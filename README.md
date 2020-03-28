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
