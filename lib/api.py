from lib import scrapper


def details(app_id):
    return scrapper.AppStoreCrawler().details(app_id=app_id)


def search(query):
    return scrapper.AppStoreCrawler().search(query=query)


def suggest(query):
    return scrapper.AppStoreCrawler().suggest(query=query)


def collection(type, category):
    return scrapper.AppStoreCrawler().collection(type=type, category=category)


def similar(app_id):
    return scrapper.AppStoreCrawler().similar(app_id=app_id)


def rating(app_id):
    return scrapper.AppStoreCrawler().rating(app_id=app_id)


def review(app_id):
    return scrapper.AppStoreCrawler().review(app_id=app_id)
