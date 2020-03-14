import unittest
from app_store_crawler import constant
from app_store_crawler.scrapper import AppStoreCrawler

DETAIL_KEYS = {
    'id',
    'appId',
    'title',
    'url',
    'description',
    'icon',
    'genres',
    'genreIds',
    'primaryGenre',
    'primaryGenreId',
    'contentRating',
    'languages',
    'size',
    'requiredOsVersion',
    'released',
    'updated',
    'releaseNotes',
    'version',
    'price',
    'currency',
    'free',
    'developerId',
    'developer',
    'developerUrl',
    'developerWebsite',
    'score',
    'reviews',
    'currentVersionScore',
    'currentVersionReviews',
    'screenshots',
    'ipadScreenshots',
    'appletvScreenshots',
    'supportedDevices',
}

RATING_KEYS = {
    'rating',
    'histogram',
}

REVIEW_KEY = {
  'id',
  'userName',
  'userUrl',
  'version',
  'score',
  'title',
  'text',
  'url'
}

class CrawlerTestBase(unittest.TestCase):
    def setUp(self):
        self.s = AppStoreCrawler()

class DetailsTest(CrawlerTestBase):
    def verify(self, app_id, country='us'):
        app_data = self.s.details(app_id, country)

        if app_data:
            app_data = app_data[0]
            self.assertTrue(all(key in app_data for key in DETAIL_KEYS))
            self.assertEqual(len(DETAIL_KEYS), len(app_data.keys()))
            if app_data.get('id') == app_id:
                self.assertEqual(app_id, app_data.get('id'))
            elif app_data.get('appID') == app_id:
                self.assertEqual(app_id, app_data.get('bundleId'))
            else:
                pass
        else:
            self.assertFalse(app_data)
            self.assertEqual(0, len(app_data))

    def test_detail_market_with_id(self):
        for country in constant.markets:
            self.verify(553834731, country=country)

    def test_detail_market_with_bundle_id(self):
        for country in constant.markets:
            self.verify('com.midasplayer.apps.candycrushsaga', country=country)

    def test_detail_with_non_existing_id(self):
        for country in constant.markets:
            self.verify(550000003831, country=country)

    def test_detail_with_non_exsiting_bundle_id(self):
        for country in constant.markets:
            self.verify('com.midasplayer.apps.candycrrew32ushsaga', country=country)

    def test_detail_with_random_string(self):
        for country in constant.markets:
            self.verify('random string', country=country)

    def test_with_invalid_country(self):
        self.verify(553834731, country='hell')

class DeveloperTest(CrawlerTestBase):
    def verify(self, app_id, country):
        app_data = self.s.developers(284882218, country=country)

        for data in app_data:
            self.assertTrue(all(key in data for key in DETAIL_KEYS))
            self.assertEqual(len(DETAIL_KEYS), len(data.keys()))

        if app_data:
            app_data = app_data[0]
            self.assertTrue(all(key in app_data for key in DETAIL_KEYS))
            self.assertEqual(len(DETAIL_KEYS), len(app_data.keys()))
            if app_data.get('id') == app_id:
                self.assertEqual(app_id, app_data.get('id'))
            elif app_data.get('appID') == app_id:
                self.assertEqual(app_id, app_data.get('bundleId'))
            else:
                pass
        else:
            self.assertFalse(app_data)
            self.assertEqual(0, len(app_data))



    def test_apps_with_dev_id(self):
        for country in constant.markets:
            self.verify(284882218, country=country)

    def test_app_with_invalid_country(self):
        self.verify(284882218, country='heaven')


class SearchTermTest(CrawlerTestBase):
    def verify(self, app_data, limit):
        for data in app_data:
            self.assertTrue(all(key in data for key in DETAIL_KEYS))
            self.assertEqual(len(DETAIL_KEYS), len(data.keys()))

        if limit == len(app_data):
            self.assertEqual(limit, len(app_data))
        elif limit > len(app_data):
            self.assertTrue(len(app_data), int)
        else:
            print(len(app_data), limit)
            self.assertFalse(app_data)

    def test_term_with_string(self):
        for country in constant.markets:
            app_data = self.s.search('panda', limit=10, country=country)
            self.verify(app_data, 10)

    def test_term_with_int(self):
        for country in constant.markets:
            app_data = self.s.search(323, limit=10, country=country)
            self.verify(app_data, 10)

    def test_non_existing_term(self):
        for country in constant.markets:
            app_data = self.s.search('fuckinghell', limit=10, country=country)
            self.verify(app_data, 10)

    def test_term_with_exceeding_limit(self):
        for country in constant.markets:
            app_data = self.s.search('panda', limit=50000000, country=country)
            self.verify(app_data, len(app_data))

    def test_with_invalid_country(self):
        app_data = self.s.search('panda', limit=2, country='hell')
        self.verify(app_data, len(app_data))

class SuggestTest(CrawlerTestBase):
    def verify(self, term, country='us', lang='en-us'):
        terms = self.s.suggest(term, country=country, lang=lang)
        if terms:
            self.assertTrue(terms, list)
        else:
            self.assertFalse(terms)

    def test_non_exist_term(self):
        terms = self.s.suggest('fuckinghell')
        self.assertFalse(terms)

    def test_suggest_with_string(self):
        for country in constant.markets:
            self.verify('panda', country=country)

    def test_suggest_with_int(self):
        for country in constant.markets:
            self.verify(3232, country=country)

    def test_with_invalid_country(self):
        self.verify(3232, country='heaven')


class CollectionTest(CrawlerTestBase):
    def verify(self, app_data):
        for data in app_data:
            self.assertTrue(all(key in data for key in DETAIL_KEYS))

    def test_with_us_market(self):
        app_data = []
        for category in constant.category:
            app_data = self.s.collection('topmacapps', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreemacapps', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingmacapps', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidmacapps', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newfreeapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newpaidapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeipadapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingipadapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidapplications', category, 'us')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidipadapplications', category, 'us')

        self.verify(app_data)

    def test_with_ao_market(self):
        app_data = []

        for category in constant.category:
            app_data = self.s.collection('topmacapps', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreemacapps', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingmacapps', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidmacapps', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newfreeapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newpaidapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeipadapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingipadapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidapplications', category, 'ao')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidipadapplications', category, 'ao')

        self.verify(app_data)

    def test_with_ai_market(self):
        app_data = []
        for category in constant.category:
            app_data = self.s.collection('topmacapps', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreemacapps', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingmacapps', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidmacapps', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newfreeapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('newpaidapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topfreeipadapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('topgrossingipadapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidapplications', category, 'ai')

        self.verify(app_data)

        for category in constant.category:
            app_data = self.s.collection('toppaidipadapplications', category, 'ai')

        self.verify(app_data)

class SimilarTest(CrawlerTestBase):
    def verify(self, app_data):
        for data in app_data:
            self.assertTrue(all(key in data for key in DETAIL_KEYS))
            self.assertEqual(len(DETAIL_KEYS), len(data.keys()))

    def test_similar_with_id(self):
        for country in constant.markets:
            app_data = self.s.similar(553834731, country=country)
            self.verify(app_data)

    def test_similar_with_bundle_id(self):
        for country in constant.markets:
            app_data = self.s.similar('com.midasplayer.apps.candycrushsaga', country=country)
            self.verify(app_data)

    def test_similar_with_non_existing_id(self):
        for country in constant.markets:
            app_data = self.s.similar(5830987664731, country=country)
            self.verify(app_data)

    def test_similiar_with_non_existing_bundle_id(self):
        for country in constant.markets:
            app_data = self.s.similar('com.midasplayer.apps.candfewfwecrushsaga', country=country)
            self.verify(app_data)

    def test_similiar_with_random_bundle_id(self):
        for country in constant.markets:
            app_data = self.s.similar('random string', country=country)
            self.verify(app_data)

    def test_with_invalid_country(self):
        app_data = self.s.similar(553834731, country='zombieland')
        self.verify(app_data)

class RatingTest(CrawlerTestBase):
    def test_rating_with_id(self):
        for country in constant.markets:
            app_data = self.s.rating(553834731, country=country)
            self.assertTrue(all(key in app_data for key in RATING_KEYS))

    def test_rating_with_bundle_id(self):
        for country in constant.markets:
            app_data = self.s.rating('com.midasplayer.apps.candycrushsaga', country=country)
            self.assertTrue(all(key in app_data for key in RATING_KEYS))

    def test_none_exsiting_id(self):
        for country in constant.markets:
            app_data = self.s.rating(55212024214731, country=country)
            self.assertTrue(all(key in app_data for key in RATING_KEYS))

    def test_none_existing_bundle_id(self):
        for country in constant.markets:
            app_data = self.s.rating('com.midasplayer.aasfpps.candycasdfrushsaga', country=country)
            self.assertTrue(all(key in app_data for key in RATING_KEYS))

    def test_random_string(self):
        for country in constant.markets:
            app_data = self.s.rating('random string', country=country)
            self.assertTrue(all(key in app_data for key in RATING_KEYS))

    def test_with_invalid_country(self):
        app_data = self.s.rating('553834731', country='heaven')
        self.assertTrue(all(key in app_data for key in RATING_KEYS))

        app_data = self.s.rating('com.midasplayer.aasfpps.candycasdfrushsaga', country='heaven')
        self.assertTrue(all(key in app_data for key in RATING_KEYS))

class ReviewTest(CrawlerTestBase):
    def review_validation(self, app_id, country='us', page=1, sort='mostRecent'):
        app_data = self.s.review(app_id, country=country, page=page, sort=sort)
        for data in app_data:
            self.assertTrue(all(key in data for key in REVIEW_KEY))
            self.assertEqual(len(REVIEW_KEY), len(data.keys()))

    def test_most_recent_with_id(self):
        for country in constant.markets:
            self.review_validation(553834731, country=country)

    def test_most_recent_with_id_with_exceeding_page(self):
        for country in constant.markets:
            self.review_validation(553834731, country=country, page=11)

    def test_most_recent_with_id_with_negative_value(self):
        for country in constant.markets:
            self.review_validation(553834731, country=country, page=-11)

    def test_most_recent_with_bundle_id(self):
        for country in constant.markets:
            self.review_validation('com.midasplayer.apps.candycrushsaga', country=country)

    def test_most_recent_with_bundle_id_with_exceeding_page(self):
        for country in constant.markets:
            self.review_validation('com.midasplayer.apps.candycrushsaga', country=country, page=11)

    def test_most_recent_with_non_existing_id(self):
        for country in constant.markets:
            self.review_validation(55003834000731, country=country)

    def test_most_recent_with_non_existing_bundle_id(self):
        for country in constant.markets:
            self.review_validation('com.midasplfdsayer.apps.candycrusasdfhsaga', country=country)

    def test_most_recent_with_random_string(self):
        for country in constant.markets:
            self.review_validation('random string', country=country)

    def test_most_helpful_with_id(self):
        for country in constant.markets:
            self.review_validation(553834731, country=country, sort='mostHelpful')

    def test_most_helpful_with_bundle_id(self):
        for country in constant.markets:
            self.review_validation('com.midasplayer.apps.candycrushsaga', sort='mostHelpful', country=country)

    def test_most_helpful_with_non_existing_id(self):
        for country in constant.markets:
            self.review_validation(553834000731, country=country)

    def test_most_helpful_with_non_existing_bundle_id(self):
        for country in constant.markets:
            self.review_validation('com.midasplfdsayer.apps.candycrusasdfhsaga', country=country)

    def test_most_helpful_with_random_string(self):
        for country in constant.markets:
            self.review_validation('random string', country=country)

    def test_id_with_invalid_sort(self):
        for country in constant.markets:
            self.review_validation(553834731, country=country, sort='latest')

    def test_bundle_id_with_invalid_sort(self):
        for country in constant.markets:
            self.review_validation('com.midasplayer.apps.candycrushsaga', country=country, sort='latest')

    def test_with_invalid_country(self):
        self.review_validation(553834731, country='hell', sort='mostHelpful')