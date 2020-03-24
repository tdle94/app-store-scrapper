from lib import constant as c
import json
import bs4
import re
import requests
import logging

log = logging.getLogger(__name__)


def build_detail_url(app_id, country, id_field='id'):
    return '{url}?{id_field}={id}&country={country}&entity=software'.format(url=c.ID_URL, id=app_id, country=country, id_field=id_field)


def build_search_url(term):
    return '{url}?clientApplication=Software&media=software&term={term}'.format(url=c.TERM_URL, term=term)


def build_suggest_url(term):
    return '{url}?clientApplication=Software&term={term}'.format(url=c.SUGGEST_URL, term=term)


def build_similar_url(app_id, country):
    return '{url}{country}/app/id{id}#see-all/customers-also-bought-apps'.format(url=c.SIMILAR_URL, id=app_id, country=country)


def build_review_url(app_id, country, page, sort):
    return '{url}{country}/rss/customerreviews/page={page}/id={id}/sortby={sort}/json'.format(url=c.REVIEW_URL, page=page, id=app_id, sort=sort, country=country)


def build_rating_url(app_id, country):
    return '{url}{country}/customer-reviews/id{id}?displayable-kind=11'.format(url=c.RATING_URL, country=country, id=app_id)


def build_list_url(collection, category, limit, store_id):
    return '{url}{collection}/{category}/limit={limit}/json?s={storeId}'.format(url=c.LIST_URL, collection=collection, category=category, limit=limit, storeId=store_id)


def construct_app_detail_dict(result):
    return {
        'id': result.get('trackId'),
        'appId': result.get('bundleId'),
        'title': result.get('title'),
        'url': result.get('trackViewUrl'),
        'description': result.get('description'),
        'icon': result.get('artworkUrl512') or result.get('artworkUrl100') or result.get('artworkUrl60'),
        'genres': result.get('genres'),
        'genreIds': result.get('genreIds'),
        'primaryGenre': result.get('primaryGenreName'),
        'primaryGenreId': result.get('primaryGenreId'),
        'contentRating': result.get('contentAdvisoryRating'),
        'languages': result.get('languageCodesIS02A'),
        'size': result.get('fileSizeBytes'),
        'requiredOsVersion': result.get('minimumOsVersion'),
        'released': result.get('releaseData'),
        'updated': result.get('currentVersionReleaseDate') or result.get('releaseDate'),
        'releaseNotes': result.get('releaseNotes'),
        'version': result.get('version'),
        'price': result.get('price'),
        'currency': result.get('currency'),
        'free': result.get('price') == 0,
        'developerId': result.get('artistId'),
        'developer': result.get('artistName'),
        'developerUrl': result.get('artistViewUrl'),
        'developerWebsite': result.get('sellerUrl'),
        'score': result.get('averageUserRating'),
        'reviews': result.get('userRatingCount'),
        'currentVersionScore': result.get('averageUserRatingForCurrentVersion'),
        'currentVersionReviews': result.get('userRatingCountForCurrentVersion'),
        'screenshots': result.get('screenshoturls'),
        'ipadScreenshots': result.get('ipadScreenshotUrls'),
        'appletvScreenshots': result.get('appletvScreenshotUrls'),
        'supportedDevices': result.get('supportedDevices'),
    }


def determine_id_field(app_id):
    return 'bundleId' if isinstance(app_id, str) and re.search('\w+\.\w+\.\w+\.\w+', app_id) else 'id'


def parse_app_detail(result):
    try:
        results = json.loads(result).get('results')
        apps_detail = []

        for r in results:
            apps_detail.append(construct_app_detail_dict(r))
    except json.decoder.JSONDecodeError as e:
        log.error(e)
        return []

    return apps_detail


def get_ids_from_search_term(html, limit):
    try:
        json_array = json.loads(html)['bubbles']
        results = json_array[0]['results'] if json_array else []
        ids = ''

        if limit > len(results):
            limit = len(results)

        for i, result in enumerate(results[0:limit]):
            ids += result['id'] if i == limit - 1 else result['id'] + ','
        return ids
    except json.decoder.JSONDecodeError as e:
        log.error(e)
        return ''


def parse_app_suggest(result):
    xml = bs4.BeautifulSoup(result, features='html.parser')
    dicts = iter(xml.findAll('dict'))
    terms = []

    next(dicts)

    for dictionary in dicts:
        string_tags = dictionary.findChildren('string')
        if len(string_tags) > 0:
            terms.append(string_tags[0].text)

    return terms


def get_app_collection_ids(result):
    try:
        entries = json.loads(result).get('feed').get('entry', [])
        ids = []

        for entry in entries:
            if entry is not list:
                continue
            id = entry.get('id').get('attributes').get('im:id')
            if id is not None:
                ids.append(id)
    except json.decoder.JSONDecodeError as e:
        log.error(e)
        return ''

    return ids


def get_app_similar_ids(result):
    html = bs4.BeautifulSoup(result, features='html.parser')
    scripts = html.find_all('script')

    if not scripts and len(scripts) < 3:
        return []

    data = scripts[2].string.split('its.serverData=')[1]
    ids = json.loads(data).get('pageData').get('softwarePageData').get('customersAlsoBoughtApps')

    return ids


def parse_app_rating(result):
    html = bs4.BeautifulSoup(result, features='html.parser')
    total_tags = html.findAll('span', attrs={'class': 'total'})
    rating_total = html.find('span', attrs={'class': 'rating-count'}).text if html.find('span', attrs={'class': 'rating-count'}) is not None else 0
    histogram = {}

    for i, total in enumerate(total_tags):
        histogram[i+1] = total.text

    return {
        'rating': rating_total,
        'histogram': histogram
    }


def parse_app_review(result):
    try:
        result = json.loads(result).get('feed')
    except json.decoder.JSONDecodeError:
        return []

    entries = result.get('entry')
    reviews = []

    if entries is None:
        return []

    for entry in entries:
        if entry is not dict:
            continue
        reviews.append({
            'id': result.get('id').get('label'),
            'userName': result.get('author').get('name').get('label'),
            'userUrl': result.get('author').get('uri').get('label'),
            'version': entry.get('im:version').get('label'),
            'score': entry.get('im:rating').get('label'),
            'title': entry.get('title').get('label'),
            'text': entry.get('content').get('label'),
            'url': entry.get('link').get('attributes').get('href')
        })

    return reviews


def request(url, method, headers=None):
    if headers is None:
        headers = {}
    try:
        response = requests.request(method=method, url=url, headers=headers)
        if not response.status_code == requests.codes.ok:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log.error(e)
        return b''

    return response.content
