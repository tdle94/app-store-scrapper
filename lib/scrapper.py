from lib import utils
from lib.constant import markets


class AppStoreCrawler(object):
    def __init__(self):
        super().__init__()

    def details(self, app_id, country):
        id_field = utils.determine_id_field(app_id)
        url = utils.build_detail_url(app_id, country, id_field)
        result = utils.request(url, method='GET')

        return utils.parse_app_detail(result)

    def developers(self, dev_id, country):
        return self.details(dev_id, country)

    def search(self, query, limit, country, lang):
        url = utils.build_search_url(query)
        store_id = markets.get(country)

        html = utils.request(url,
                             method='GET',
                             headers={'X-Apple-Store-Front': '%s,24 t:native' % store_id, 'Accept-Language': lang})

        ids = utils.get_ids_from_search_term(html, limit)

        return self.details(ids, country)

    def suggest(self, query, country, lang):
        url = utils.build_suggest_url(query)
        store_id = markets.get(country)

        result = utils.request(url,
                               method='GET',
                               headers={'X-Apple-Store-Front': '%s,24 t:native' % store_id, 'Accept-Language': lang})
        return utils.parse_app_suggest(result)

    def collection(self, type, category, country, limit):
        store_id = markets.get(country)
        url = utils.build_list_url(type, category, limit, store_id)

        result = utils.request(url, method='GET')

        ids = utils.get_app_collection_ids(result)

        return self.details(','.join(ids), country)

    def similar(self, app_id, country):
        url = utils.build_similar_url(app_id, country=country)
        store_id = markets.get(country)
        result = utils.request(url,
                               method='GET',
                               headers={'X-Apple-Store-Front': '%s,32' % store_id})

        ids = utils.get_app_similar_ids(result)

        return self.details(','.join(ids), country)

    def rating(self, app_id, country):
        app_id = self.get_correct_app_id(app_id, country)
        url = utils.build_rating_url(app_id, country)
        store_id = markets.get(country)

        result = utils.request(url,
                               method='GET',
                               headers={'X-Apple-Store-Front': '%s,12' % store_id})

        return utils.parse_app_rating(result)

    def review(self, app_id, country, page, sort):
        app_id = self.get_correct_app_id(app_id, country)
        url = utils.build_review_url(app_id, country, page, sort)

        result = utils.request(url, method='GET')

        return utils.parse_app_review(result)

    def get_correct_app_id(self, app_id, country):
        field_id = utils.determine_id_field(app_id)
        if field_id == 'bundleId':
            app_detail = self.details(app_id, country)
            if app_detail:
                app_id = app_detail[0].get('id')

        return app_id
