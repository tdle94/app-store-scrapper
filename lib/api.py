from lib import scrapper

def details(app_id):
    s = scrapper.AppStoreScrapper()
    return s.details(app_id)

def search(query):
    s = scrapper.AppStoreScrapper()
    return s.search(query)

def suggest(query):
    s = scrapper.AppStoreScrapper()
    return s.suggest(query)

def collection(type, category):
    s = scrapper.AppStoreScrapper()
    return s.collection(type, category)

def similar(app_id):
    s = scrapper.AppStoreScrapper()
    return s.similar(app_id)

def rating(app_id):
    s = scrapper.AppStoreScrapper()
    return s.rating(app_id)

def review(app_id):
    s = scrapper.AppStoreScrapper()
    return s.review(app_id)
