# app-store-scrapper
light weight library to scrape data from itune

## Installation

install with pip

```pip install app-store-scrapper```

## Usage

- details: Fetch application detail.
- search: Fetch applications matching a search query.
- suggest: Fetch a list of query string suggestions.
- collection: Fetch a list of applications and their details.
- similar: Fetch an application's similar apps.
- rating: Retrieves the ratings for the app.
- review: Retrieves a page of reviews for the app.

**app**

Retrieves the full detail of an application. Options:

  - ```id```: the iTunes "trackId" of the app, for example ```553834731``` for Candy Crush Saga. Either this or the ```appId``` should be provided.
  - ```appId```: the iTunes "bundleId" of the app, for example com.midasplayer.apps.candycrushsaga for Candy Crush Saga. Either this or the id should be provided.
  - ```country```: the two letter country code to get the app details from. Defaults to us. Note this also affects the language of the data.
  - ```ratings```: load additional ratings information like ratings number and histogram
  
```python
>>> from lib import scrapper
>>> scrapper.AppStoreCrawler().details(553834731, 'us')
[
  {
    'id': 553834731,
    'appId': 'com.midasplayer.apps.candycrushsaga',
    'title': None,
    'url': 'https://apps.apple.com/us/app/candy-crush-saga/id553834731?uo=4',
    'description': "Start playing\xa0Candy Crush Saga\xa0today –\xa0a legendary\xa0puzzle game\xa0loved by millions of players around the world.\n\nWith over a trillion\xa0levels\xa0played, this\xa0sweet\xa0match 3\xa0puzzle game\xa0is one of the most\xa0popular\xa0mobile\xa0games\xa0of all time!\n\nSwitch and match Candies in this\xa0tasty\xa0puzzle\xa0adventure\xa0to progress to the next level for that sweet winning feeling! Solve\xa0puzzles\xa0with quick thinking and smart moves, and be rewarded with delicious rainbow-colored cascades and tasty candy combos!\n\nPlan your moves by\xa0matching 3\xa0or more candies in a row, using boosters wisely in order to overcome those extra sticky\xa0puzzles!\xa0Blast\xa0the chocolate and collect\xa0sweet\xa0candy\xa0across thousands of\xa0levels,\xa0guaranteed to have you craving more!\n\nCandy Crush Saga features:\n\nTHE GAME THAT KEEPS YOU CRAVING MORE\nThousands of the\xa0best levels\xa0and\xa0puzzles\xa0in the\xa0Candy\xa0Kingdom and with more added every 2 weeks your sugar fix is never far away!\xa0\n\nMANY WAYS TO WIN REWARDS\nCheck back daily and spin the Daily Booster Wheel to receive\xa0free\xa0tasty rewards, and take part in time limited challenges to earn\xa0boosters\xa0to help you\xa0level\xa0up!\xa0\n\n\xa0VARIETY OF SUGAR-COATED CHALLENGES\nSweet ways to play:\xa0Game\xa0modes including Target Score, Clear the Jelly, Collect the Ingredients and Order Mode\n\nPLAY ALONE OR WITH FRIENDS\nGet to the\xa0top\xa0of the leaderboard events and compare scores with\xa0friends\xa0and competitors!\n\nLevels\xa0range from\xa0easy\xa0to\xa0hard\xa0for all\xa0adults\xa0to enjoy – accessible on-the-go,\xa0offline\xa0and\xa0online.\nIt's easy to sync the\xa0game\xa0between devices and unlock full game features when connected to the Internet or\xa0Wifi.\nFollow us to get news and updates; facebook.com/CandyCrushSaga, Twitter @CandyCrushSaga, Youtube\xa0https://www.youtube.com/user/CandyCrushOfficial\nVisit\xa0https://community.king.com/en/candy-crush-saga\xa0to access the Community and competitions!\nCandy Crush Saga\xa0is completely\xa0free\xa0to play but some optional in-game items will require payment.\nYou can turn off the payment feature by disabling in-app purchases in your device’s settings.\nBy downloading this\xa0game\xa0you are agreeing to our terms of service;\xa0http://about.king.com/consumer-terms/terms\n\nDo not sell my data: King shares your personal information with advertising partners to personalize ads. Learn more at https://king.com/privacyPolicy.  If you wish to exercise your Do Not Sell My Data rights, you can do so by contacting us via the in game help centre or by going to https://soporto.king.com/\n\nHave fun playing\xa0Candy Crush Saga\xa0the sweetest\xa0match 3\xa0puzzle game\xa0around!\xa0\nIf you enjoy playing\xa0Candy Crush Saga, you may also enjoy its sister\xa0puzzle games;\xa0Candy Crush\xa0Soda\xa0Saga, Candy Crush\xa0Jelly\xa0Saga\xa0and\xa0Candy Crush\xa0Friends\xa0Saga!",
    'icon': 'https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/ab/1d/30/ab1d309c-e992-fde1-dd24-a05a536122be/source/512x512bb.jpg',
    'genres': ['Games', 'Entertainment', 'Puzzle', 'Casual'],
    'genreIds': ['6014', '6016', '7012', '7003'],
    'primaryGenre': 'Games', 'primaryGenreId': 6014, 'contentRating': '4+', 'languages': None, 'size': '274406400', 
    'requiredOsVersion': '9',
    'released': None,
    'updated': '2020-03-26T15:15:19Z',
    'releaseNotes': "We hope you’re having fun playing Candy Crush Saga! We update the game every week so don't forget to download the latest version to get all the sweet new features and levels!\n\nNew to the game? Don’t be shy, join the fun! \n\nComing back after a break? About time! \n\nLet’s play!",
    'version': '1.173.0.2',
    'price': 0.0,
    'currency': 'USD',
    'free': True,
    'developerId': 526656015,
    'developer': 'King',
    'developerUrl': 'https://apps.apple.com/us/developer/king/id526656015?uo=4',
    'developerWebsite': 'http://candycrushsaga.com/',
    'score': 4.69902,
    'reviews': 1367860,
    'currentVersionScore': 4.69902,
    'currentVersionReviews': 1367860,
    'screenshots': None,
    'ipadScreenshots': ['https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/cb/2b/fb/cb2bfb5d-3fa6-7b4a-34f6-dd436f81a4f9/pr_source.jpg/552x414bb.jpg', 'https://is5-ssl.mzstatic.com/image/thumb/Purple123/v4/2b/01/1a/2b011aa9-0593-a782-977d-ebf83c1a0216/pr_source.jpg/552x414bb.jpg', 'https://is5-ssl.mzstatic.com/image/thumb/Purple123/v4/bc/ee/e6/bceee65a-1043-6c41-03fb-774a7e19bdeb/pr_source.jpg/552x414bb.jpg', 'https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/d8/f8/55/d8f85583-f48d-59a7-db54-96b0407f7108/pr_source.jpg/552x414bb.jpg', 'https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/cb/51/d1/cb51d12d-e118-ae59-c36d-63ac0bae1faa/pr_source.jpg/552x414bb.jpg', 'https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/56/77/c2/5677c21d-6222-87f9-f052-8686607acd21/mzl.zdiinuds.jpg/552x414bb.jpg'],
    'appletvScreenshots': [],
    'supportedDevices': ['iPad2Wifi-iPad2Wifi', 'iPadAir2-iPadAir2', 'iPadMiniRetinaCellular-iPadMiniRetinaCellular', 'iPadAir2Cellular-iPadAir2Cellular', 'iPhone11ProMax-iPhone11ProMax', 'iPad878-iPad878', 'iPodTouchSeventhGen-iPodTouchSeventhGen', 'iPadMini-iPadMini', 'iPad73-iPad73', 'iPodTouchFifthGen-iPodTouchFifthGen', 'iPhone6sPlus-iPhone6sPlus', 'iPad834-iPad834', 'iPadMini3Cellular-iPadMini3Cellular', 'iPadPro97-iPadPro97', 'iPadThirdGen-iPadThirdGen', 'iPadProCellular-iPadProCellular', 'iPadAir-iPadAir', 'iPhoneSE-iPhoneSE', 'iPadMini4G-iPadMini4G', 'iPhone5c-iPhone5c', 'iPadAir3-iPadAir3', 'iPhone8-iPhone8', 'iPadMini4Cellular-iPadMini4Cellular', 'iPhone7-iPhone7', 'iPhoneXR-iPhoneXR', 'iPadAir3Cellular-iPadAir3Cellular', 'iPad856-iPad856', 'iPhone11Pro-iPhone11Pro', 'iPhone5-iPhone5', 'iPhone11-iPhone11', 'iPadPro97Cellular-iPadPro97Cellular', 'iPad75-iPad75', 'iPhoneXSMax-iPhoneXSMax', 'iPhone5s-iPhone5s', 'iPhone7Plus-iPhone7Plus', 'iPadMini3-iPadMini3', 'iPhone4S-iPhone4S', 'iPadSeventhGenCellular-iPadSeventhGenCellular', 'iPadFourthGen-iPadFourthGen', 'iPadFourthGen4G-iPadFourthGen4G', 'iPhone8Plus-iPhone8Plus', 'iPad23G-iPad23G', 'iPadMini5-iPadMini5', 'iPad71-iPad71', 'iPhoneX-iPhoneX', 'iPadMini4-iPadMini4', 'iPodTouchSixthGen-iPodTouchSixthGen', 'iPad74-iPad74', 'iPhoneXS-iPhoneXS', 'iPad812-iPad812', 'iPadPro-iPadPro', 'iPadMini5Cellular-iPadMini5Cellular', 'iPadThirdGen4G-iPadThirdGen4G', 'iPadAirCellular-iPadAirCellular', 'iPhone6s-iPhone6s', 'iPadSeventhGen-iPadSeventhGen', 'iPad72-iPad72', 'iPhone6-iPhone6', 'iPhone6Plus-iPhone6Plus', 'iPad612-iPad612', 'iPadMiniRetina-iPadMiniRetina', 'iPad611-iPad611', 'iPad76-iPad76']
  }
]
```
