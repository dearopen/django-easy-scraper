import re


def get_domain_name(url):
    domain_name_pat = re.compile(r'.*\://(?:www.)?([^\/]+)')
    extract = domain_name_pat.findall(url)

    if len(extract) == 0:
        raise ValueError("Invalid domain name !! We couldn't parse domain name from your given url")
    else:
        return extract[0]



class BaseSwitch(object):
    """
        Switer dict should be like following this:

        'example.com': MyScraperClass.regex_url_scrape

        Above you meant, first one will be domain name you are scraping and last one will be class method rregex_url_scrape
    """
    switcher = {}

    @classmethod
    def get_data(self, url, raise_exception=False):
        domain = get_domain_name(url)

        if not domain in self.switcher:
            raise NotImplementedError(url)
        return self.switcher.get(domain)(url, raise_exception)

