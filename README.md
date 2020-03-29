# app-store-scrapper
light weight library to scrape data from itune

## Installation

install with pip

```pip install appstorescrapper```

## Usage

- [details](https://github.com/tdle94/app-store-scrapper#details): Fetch application detail.
- [search](https://github.com/tdle94/app-store-scrapper#search): Fetch applications matching a search query.
- [developer](https://github.com/tdle94/app-store-scrapper#developer): Retrieve a list of apps given by developer id.
- suggest: Fetch a list of query string suggestions.
- collection: Fetch a list of applications and their details.
- similar: Fetch an application's similar apps.
- rating: Retrieves the ratings for the app.
- review: Retrieves a page of reviews for the app.

#### details

Retrieves the full detail of an application. Options:

  - ```id```: the iTunes "trackId" of the app, for example ```553834731``` for Candy Crush Saga. Either this or the ```app_id``` should be provided.
  - ```app_id```: the iTunes "bundleId" of the app, for example com.midasplayer.apps.candycrushsaga for Candy Crush Saga. Either this or the id should be provided.
  - ```country```: the two letter country code to get the app details from. Defaults to us. Note this also affects the language of the data.
  
```python
>>> from lib import api
>>> api.details(553834731)
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

#### developer

Retrieves a list of applications by the give developer id. Options:

  - ```dev_id```: the iTunes "artistId" of the developer, for example 284882218 for Facebook.
  - ```country```: the two letter country code to get the app details from. Defaults to us. Note this also affects the language of the data.
  
```python
>>> from lib import api
>>> api.developer(284882218)
[
   {
      "id":"None",
      "appId":"None",
      "title":"None",
      "url":"None",
      "description":"None",
      "icon":"None",
      "genres":"None",
      "genreIds":"None",
      "primaryGenre":"None",
      "primaryGenreId":"None",
      "contentRating":"None",
      "languages":"None",
      "size":"None",
      "requiredOsVersion":"None",
      "released":"None",
      "updated":"None",
      "releaseNotes":"None",
      "version":"None",
      "price":"None",
      "currency":"None",
      "free":False,
      "developerId":284882218,
      "developer":"Facebook, Inc.",
      "developerUrl":"None",
      "developerWebsite":"None",
      "score":"None",
      "reviews":"None",
      "currentVersionScore":"None",
      "currentVersionReviews":"None",
      "screenshots":"None",
      "ipadScreenshots":"None",
      "appletvScreenshots":"None",
      "supportedDevices":"None"
   },
   {
      "id":284882215,
      "appId":"com.facebook.Facebook",
      "title":"None",
      "url":"https://apps.apple.com/us/app/facebook/id284882215?uo=4",
      "description":"Connect with friends, family and people who share the same interests as you. Communicate privately, watch your favorite content, buy and sell items or just spend time with your community. On Facebook, keeping up with the people who matter most is easy. Discover, enjoy and do more together.\n  \nStay up to date with your loved ones:\n  • Share what's on your mind, announce major life events through posts and celebrate the everyday moments with Stories.\n  • Express yourself through your profile and posts, watch, react, interact and stay in touch with your friends, throughout\n  the day.\n\nConnect with people who share your interests with Groups:\n  • With tens of millions of groups, you'll find something for all your interests and discover more groups relevant to you.\n  • Use the Groups tab as a hub to quickly access all your groups content. Find relevant groups based on your interests with the new discovery tool and recommendations.\n\nBecome more involved with your community:\n  • Discover events happening near you, businesses to support, local groups and activities to be part of.\n  • Check out local recommendations from your friends, then coordinate with them and make plans to get together.\n  • Raise funds for a cause that’s important to you, mentor someone who wants help achieving their goals and, in the event of a local crisis, connect with other people to find or give supplies, food or shelter.\n\nEnjoy entertainment together with Watch:\n  • Discover all kinds of content from original shows to creators to trending videos in topics like beauty, sports, and entertainment.\n  • Join conversations, share with others, interact with viewers and creators and watch together like never before.\n\nBuy and sell with Marketplace:\n  • Whether it's an everyday or one-of-a-kind item, you can discover everything from household items to your next car or apartment on Marketplace.\n  • List your own item for sale and conveniently communicate with buyers and sellers through Messenger \n\nRead our Data Use Policy, Terms and other important info in the legal section of our App Store description. \n\nContinued use of GPS running in the background can dramatically decrease battery life. Facebook doesn't run GPS in the background unless you give us permission by turning on optional features that require this.",
      "icon":"https://is1-ssl.mzstatic.com/image/thumb/Purple113/v4/e5/d6/79/e5d6794b-09ca-5c9d-3e26-72229f41775c/source/512x512bb.jpg",
      "genres":[
         "Social Networking"
      ],
      "genreIds":[
         "6005"
      ],
      "primaryGenre":"Social Networking",
      "primaryGenreId":6005,
      "contentRating":"12+",
      "languages":"None",
      "size":"410391552",
      "requiredOsVersion":"10.0",
      "released":"None",
      "updated":"2020-03-26T16:01:04Z",
      "releaseNotes":"We update the app regularly so we can make it better for you. Get the latest version for all of the available Facebook features. This version includes several bug fixes and performance improvements.",
      "version":"263.0",
      "price":0.0,
      "currency":"USD",
      "free":True,
      "developerId":284882218,
      "developer":"Facebook, Inc.",
      "developerUrl":"https://apps.apple.com/us/developer/facebook-inc/id284882218?uo=4",
      "developerWebsite":"http://www.facebook.com/mobile",
      "score":3.12285,
      "reviews":419213,
      "currentVersionScore":3.12285,
      "currentVersionReviews":419213,
      "screenshots":"None",
      "ipadScreenshots":[
         "https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/a2/ff/e2/a2ffe2cd-22f0-fdd9-0dbb-58a3d5bc1c23/mzl.ghlgunye.png/576x768bb.png",
         "https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/90/9c/36/909c363a-a230-f747-1e6d-bda15a1f19c3/mzl.ouqckawq.png/552x414bb.png",
         "https://is5-ssl.mzstatic.com/image/thumb/Purple113/v4/49/8e/3f/498e3fa7-19e9-93df-e5ba-8c549747a921/mzl.xbivmonc.png/576x768bb.png"
      ],
      "appletvScreenshots":[],
      "supportedDevices":[ "iPadMini3-iPadMini3", "iPhone7-iPhone7", "iPad76-iPad76", "iPadFourthGen4G-iPadFourthGen4G", "iPadMiniRetina-iPadMiniRetina", "iPad878-iPad878", "iPadAir2-iPadAir2", "iPadPro-iPadPro", "iPad75-iPad75", "iPhone6s-iPhone6s", "iPhoneX-iPhoneX", "iPhone6-iPhone6", "iPhoneXR-iPhoneXR", "iPhone5-iPhone5", "iPadMini4-iPadMini4", "iPadSeventhGen-iPadSeventhGen", "iPadAir2Cellular-iPadAir2Cellular", "iPhoneSE-iPhoneSE", "iPadMini4Cellular-iPadMini4Cellular", "iPad611-iPad611", "iPad856-iPad856", "iPhoneXSMax-iPhoneXSMax", "Watch4-Watch4", "iPodTouchSixthGen-iPodTouchSixthGen", "iPadFourthGen-iPadFourthGen", "iPhoneXS-iPhoneXS", "Watch5-Watch5", "iPadProCellular-iPadProCellular", "iPhone11-iPhone11", "iPhone6sPlus-iPhone6sPlus", "iPadAirCellular-iPadAirCellular", "iPhone11ProMax-iPhone11ProMax", "iPad812-iPad812", "iPad72-iPad72", "iPad834-iPad834", "iPadMini5Cellular-iPadMini5Cellular", "iPadAir3Cellular-iPadAir3Cellular", "iPad612-iPad612", "iPhone8-iPhone8", "iPadPro97-iPadPro97", "iPadMini5-iPadMini5", "iPhone8Plus-iPhone8Plus", "iPhone5s-iPhone5s", "iPad73-iPad73", "iPhone5c-iPhone5c", "iPad71-iPad71", "iPadAir3-iPadAir3","iPhone11Pro-iPhone11Pro", "iPhone7Plus-iPhone7Plus", "iPodTouchSeventhGen-iPodTouchSeventhGen", "iPadMini3Cellular-iPadMini3Cellular", "iPadSeventhGenCellular-iPadSeventhGenCellular", "iPadPro97Cellular-iPadPro97Cellular", "iPhone6Plus-iPhone6Plus", "iPadMiniRetinaCellular-iPadMiniRetinaCellular", "iPad74-iPad74", "iPadAir-iPadAir"]
   },
   ...
]
```

#### search

Retrieves a list of apps that results of searching by the given term. Options:

- ```query```: the term to search for (required).
- ```limit```: the amount of elements to retrieve. Defaults to 10.
- ```country```: the two letter country code to get the similar apps from. Defaults to us.
- ```lang```: language code for the result text. Defaults to en-us.

```python
>>> from lib import api
>>> api.search('panda', limit=2)
[
  {
    'id': 903990394,
    'appId': 'com.pandarg.pxmobileapp',
    'title': None,
    'url': 'https://apps.apple.com/us/app/panda-express/id903990394?uo=4',
    'description': 'Satisfying your Orange Chicken craving just got easier with the new Panda Express app. Order ahead, find your nearest location and set your preferences. Bonus: Running late? Just let us know through the app and your order will be hot when you’re ready for it.',
    'icon': 'https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/88/1d/a3/881da39f-1bd2-4773-9762-ece2791ef62b/source/512x512bb.jpg',
    'genres': ['Food & Drink'],
    'genreIds': ['6023'],
    'primaryGenre': 'Food & Drink',
    'primaryGenreId': 6023,
    'contentRating': '4+',
    'languages': None,
    'size': '105432064',
    'requiredOsVersion': '10.0',
    'released': None,
    'updated': '2020-03-24T16:48:41Z',
    'releaseNotes': 'Displays limit of two family meals per order.',
    'version': '2.14',
    'price': 0.0,
    'currency': 'USD',
    'free': True,
    'developerId': 903990397,
    'developer': 'Panda Express',
    'developerUrl': 'https://apps.apple.com/us/developer/panda-express/id903990397?uo=4',
    'developerWebsite': 'https://www.pandaexpress.com',
    'score': 4.59747,
    'reviews': 35582,
    'currentVersionScore': 4.59747,
    'currentVersionReviews': 35582,
    'screenshots': None,
    'ipadScreenshots': [],
    'appletvScreenshots': [],
    'supportedDevices': ['iPhone7Plus-iPhone7Plus', 'iPad611-iPad611', 'iPadMini4Cellular-iPadMini4Cellular', 'iPad72-iPad72', 'iPad74-iPad74', 'iPadAir3-iPadAir3', 'iPhoneXSMax-iPhoneXSMax', 'iPadPro97Cellular-iPadPro97Cellular', 'iPhone5s-iPhone5s', 'iPad71-iPad71', 'iPadAir2Cellular-iPadAir2Cellular', 'iPad856-iPad856', 'iPadMini5-iPadMini5', 'iPhone5c-iPhone5c', 'iPadFourthGen4G-iPadFourthGen4G', 'iPadMini3Cellular-iPadMini3Cellular', 'iPadMini3-iPadMini3', 'iPhoneSE-iPhoneSE', 'iPhoneXR-iPhoneXR', 'iPadProCellular-iPadProCellular', 'iPadFourthGen-iPadFourthGen', 'iPadAir3Cellular-iPadAir3Cellular', 'iPhone11-iPhone11', 'iPad76-iPad76', 'iPad612-iPad612', 'iPadPro-iPadPro', 'iPodTouchSixthGen-iPodTouchSixthGen', 'iPad834-iPad834', 'iPad75-iPad75', 'iPadSeventhGenCellular-iPadSeventhGenCellular', 'iPadSeventhGen-iPadSeventhGen', 'iPadAir2-iPadAir2', 'iPadMini5Cellular-iPadMini5Cellular', 'iPhone5-iPhone5', 'iPad878-iPad878', 'iPad73-iPad73', 'iPhone6Plus-iPhone6Plus', 'iPadPro97-iPadPro97', 'iPadMiniRetina-iPadMiniRetina', 'iPhone11ProMax-iPhone11ProMax', 'iPodTouchSeventhGen-iPodTouchSeventhGen', 'iPhoneXS-iPhoneXS', 'iPhone6s-iPhone6s', 'iPhone8Plus-iPhone8Plus', 'iPhone8-iPhone8', 'iPhone6-iPhone6', 'iPadAirCellular-iPadAirCellular', 'iPhone6sPlus-iPhone6sPlus', 'iPadMiniRetinaCellular-iPadMiniRetinaCellular', 'iPhone11Pro-iPhone11Pro', 'iPhoneX-iPhoneX', 'iPadAir-iPadAir', 'iPhone7-iPhone7', 'iPadMini4-iPadMini4', 'iPad812-iPad812']},
    {
      'id': 1250583288,
      'appId': 'com.pandaaf.app',
      'title': None,
      'url': 'https://apps.apple.com/us/app/panda/id1250583288?uo=4',
      'description': 'Panda is a new kind of TV show starring you and your friends. Record and watch new episodes together each week until the season is over.\n\nCreate an avatar, invite friends, record scenes, and start watching your show now!\n\nNeed help?\nReach out to us anytime on Twitter @pandastartup or feedback@panda.af',
      'icon': 'https://is4-ssl.mzstatic.com/image/thumb/Purple124/v4/f6/40/5a/f6405a90-f8e0-80ce-2490-4d2f48d77dff/source/512x512bb.jpg',
      'genres': ['Entertainment', 'Photo & Video'],
      'genreIds': ['6016', '6008'],
      'primaryGenre': 'Entertainment',
      'primaryGenreId': 6016,
      'contentRating': '12+',
      'languages': None,
      'size': '155659264',
      'requiredOsVersion': '12.0',
      'released': None,
      'updated': '2020-02-13T15:16:29Z',
      'releaseNotes': "2.1.2 fixes pesky bugs!\n\n-Fixed issues around downloading episodes \n-Fixed characters not loading into scenes at times\n-Fixed bugs around account creation\n-Fixed various bugs around sending and receiving invites\n-Fixed audio playing out of speakers when using AirPods\n-Fixed the disappearing progress bar bug\n-Reshooting your lines is a smoother process now\n-There is now the ability to download videos! Easier to share your best moments (and more to come soon)\n\nLong video processing times are being fixed in the following update.\n\nWe've got a ton more fixes and features coming soon.\n\nStay tuned for new episodes every friday!",
      'version': '2.1.2',
      'price': 0.0,
      'currency': 'USD',
      'free': True,
      'developerId': 1250583287,
      'developer': 'Panda Squad',
      'developerUrl': 'https://apps.apple.com/us/developer/panda-squad/id1250583287?uo=4',
      'developerWebsite': 'https://panda.af',
      'score': 3.58962,
      'reviews': 212,
      'currentVersionScore': 3.58962,
      'currentVersionReviews': 212,
      'screenshots': None,
      'ipadScreenshots': [],
      'appletvScreenshots': [],
      'supportedDevices': ['iPhone7Plus-iPhone7Plus', 'iPad611-iPad611', 'iPadMini4Cellular-iPadMini4Cellular', 'iPad72-iPad72', 'iPad74-iPad74', 'iPadAir3-iPadAir3', 'iPhoneXSMax-iPhoneXSMax', 'iPadPro97Cellular-iPadPro97Cellular', 'iPhone5s-iPhone5s', 'iPad71-iPad71', 'iPadAir2Cellular-iPadAir2Cellular', 'iPad856-iPad856', 'iPadMini5-iPadMini5', 'iPadMini3Cellular-iPadMini3Cellular', 'iPadMini3-iPadMini3', 'iPhoneSE-iPhoneSE', 'iPhoneXR-iPhoneXR', 'iPadProCellular-iPadProCellular', 'iPadAir3Cellular-iPadAir3Cellular', 'iPhone11-iPhone11', 'iPad76-iPad76', 'iPad612-iPad612', 'iPadPro-iPadPro', 'iPodTouchSixthGen-iPodTouchSixthGen', 'iPad834-iPad834', 'iPad75-iPad75', 'iPadSeventhGenCellular-iPadSeventhGenCellular', 'iPadSeventhGen-iPadSeventhGen', 'iPadAir2-iPadAir2', 'iPadMini5Cellular-iPadMini5Cellular', 'iPad878-iPad878', 'iPad73-iPad73', 'iPhone6Plus-iPhone6Plus', 'iPadPro97-iPadPro97', 'iPadMiniRetina-iPadMiniRetina', 'iPhone11ProMax-iPhone11ProMax', 'iPodTouchSeventhGen-iPodTouchSeventhGen', 'iPhoneXS-iPhoneXS', 'iPhone6s-iPhone6s', 'iPhone8Plus-iPhone8Plus', 'iPhone8-iPhone8', 'iPhone6-iPhone6', 'iPadAirCellular-iPadAirCellular', 'iPhone6sPlus-iPhone6sPlus', 'iPadMiniRetinaCellular-iPadMiniRetinaCellular', 'iPhone11Pro-iPhone11Pro', 'iPhoneX-iPhoneX', 'iPadAir-iPadAir', 'iPhone7-iPhone7', 'iPadMini4-iPadMini4', 'iPad812-iPad812']
  }
]
```


