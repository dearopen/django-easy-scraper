# Django Easy Scraper

An standalone django app that can be used/intigrated with both django and no-django application easily. the scraping mechanism is fully based on `Regular Expression` but you can extends based on what you are familiar with very easily.

It requires to install python `requests` modules


## Install

`pip install django-easy-scraper`

## Basic Uses

```
from django_easy_scraper import scraper

class ScrapeExampleDotCom(scraper.Scraper):

    regex_fields = {
        'price': "Write Your Regex pattern for price here",
        'title': "Write your regex pattern for title here",
        # Like above way you can add as much fields/keys as you want
    }

```

### Scrape now
```
url = 'www.example.com/bla-bla-details-page/
data = ScrapeExampleDotCom.regex_url_scraper(url)

print(data)
```
and the response should look like this if your regex pattern are correct:
```
{
    'price': 4,
    'title': 'an scraped title',
}
```

`regex_url_scraper` method always gives you json response,

So if you add many regex pattern in `regex_fields`, it will give you response that number of json key with result that you added in that fields.


# Multiple Sites Scraping together

You don't need to call different method for different site all the time !! Just call once and scrape all, something fun, right?

### Like you are gonna scrape four sites:
> www.example.com

> www.amazonxsite.com

> www.newyorktimesnoexist.com

> www.walmaaaart.com

But how will those site product scrape automatically, curious ? 

- Wirte Regex patter for all above site and fields/data you want:


```
from django_easy_scraper import scraper

class ScrapeExampleDotCom(scraper.Scraper):
    regex_fields = {
        'price': "Write Your Regex pattern for price here",
        'title': "Write your regex pattern for title here",
        # Like above way you can add as much fields/keys as you want
    }

class ScrapeAmazonxSite(scraper.Scraper):
    regex_fields = {
        'price': "Write Your Regex pattern for price here",
        'title': "Write your regex pattern for title here",
        # Like above way you can add as much fields/keys as you want
    }

class ScrapeNewYorkTimeNoExist(scraper.Scraper):
    regex_fields = {
        'price': "Write Your Regex pattern for price here",
        'title': "Write your regex pattern for title here",
        # Like above way you can add as much fields/keys as you want
    }

class ScrapeWalmaaartDotCom(scraper.Scraper):
    regex_fields = {
        'price': "Write Your Regex pattern for price here",
        'title': "Write your regex pattern for title here",
        # Like above way you can add as much fields/keys as you want
    }

```


You have written regular expression for you all the site you are gonna scrape,

Now it's time use your `Switch` class that will route your script/class based on the site you are gonna scrape? It's complex? No !!

Here where the magic begins:

Just place all your class in the dict.


> Important Note:

`key` name should be domain name, pure domain name, no www or http or slash, dont add anything prefix/suffix
`value` should be the class of that domain you have written for and place it's method `regex_url_scraper

```
from django_easy_scraper import switch

class Switch(switch.BaseSwitch):
    switcher = {
        'amazonxsite.com': ScrapeElgiganten.regex_url_scraper,
        'amazonxsite.com': ScrapeAmazonxSite.regex_url_scraper,
        'newyorktimesnoexist.com': ScrapeNewYorkTimeNoExist.regex_url_scraper,
        'walmaaaart.com': ScrapeWalmaaartDotCom.regex_url_scraper,
    }

```

So you have done routing your script/class based on the url it gets.

### Get response data as json like above site:

```
url = 'Any of site you have written class for the site and added in switch class'

response = Switch.get_data(url=url, raise_exception=False)

print(response) # Will give you an object of data that you trying to scrape

```

Switch class is giving you facilities to route your scraping class automacally based whatever site link pass to it's method.


### Got an issue ?
Please open an issue on our github repo: https://github.com/dearopen/django-easy-scraper

Don't forget to star to this project if you like this.

Happy Scraping !!