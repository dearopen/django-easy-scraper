import re
import csv
from html import unescape

import requests

from lxml import html


def get_page_content(url):
    response = requests.get(url)
    return response.text

class Scraper(object):
    """
    regex_fields will take following items - 
        fields_name: '<regex pattern>'
    """
    regex_fields = {}


    """
    xpath_fields will take following items - 
        fields_name: '<regex pattern>'
    """
    xpath_fields = {}

    @classmethod
    def regex_url_scraper(self, url, raise_exception=False):
        if not self.regex_fields:
            raise ValueError("regex_fields dictionary can't remain blank if you use regex_url_scraper()")

        content = get_page_content(url)

        scrapped = {}
        for field, pattern in self.regex_fields.items():
            result = re.findall(pattern, content)
            if len(result) == 0:
                if raise_exception:
                    raise LookupError(field)
                else:
                    scrapped[field] = ''
            else:
                scrapped[field] = result[0]

        return scrapped


    @classmethod
    def xpath_scraper(self, url, raise_exception=False):
        if not self.xpath_fields:
            raise ValueError("xpath_fields dictionary can't remain blank if you use xpath_scrape()")
        content = get_page_content(url)

        tree = html.fromstring(content)

        scrapped = {}
        for field, pattern in self.xpath_fields.items():
            result = tree.xpath(pattern)

            if len(result) == 0:
                if raise_exception:
                    raise LookupError(field)
                else:
                    scrapped[field] = ''
            else:
                scrapped[field] = result[0]

        return scrapped
