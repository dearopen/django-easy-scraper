import re
import csv
from html import unescape
import requests


def get_page_content(url):
    response = requests.get(url)
    return response.text

class Scraper(object):
    """
    egex_fields will take these following items - 
        fields_name: '<regex pattern>'
    """
    regex_fields = {}

    @classmethod
    def regex_url_scraper(self, url):
        content = get_page_content(url)

        scrapped = {}
        for field, pattern in self.regex_fields.items():
            result = re.findall(pattern, content)
            if len(result) == 0:
                raise LookupError(field)
            else:
                scrapped[field] = result[0]

        return scrapped