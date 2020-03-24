from lib import scrapper


def details(app_id, country='us'):
    return scrapper.AppStoreCrawler().details(app_id=app_id, country=country)


def search(query, country='us', lang='en-us'):
    return scrapper.AppStoreCrawler().search(query=query, country=country, lang=lang)


def suggest(query, country='us', lang='en-us'):
    return scrapper.AppStoreCrawler().suggest(query=query, country=country, lang=lang)


def collection(type, category, country='us', limit=50):
    return scrapper.AppStoreCrawler().collection(type=type, category=category, country=country, limit=limit)


def similar(app_id, country='us'):
    return scrapper.AppStoreCrawler().similar(app_id=app_id, country=country)


def rating(app_id, country='us'):
    return scrapper.AppStoreCrawler().rating(app_id=app_id, country=country)


def review(app_id, country='us', page=1, sort='mostRecent'):
    return scrapper.AppStoreCrawler().review(app_id=app_id, country=country, page=page, sort=sort)
