
from urllib.request import urlopen, Request

from lxml import html

from .processor import Processor
from .helpers import safe_element_value, sanitize_price, AGENT


class Americanas(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        request = Request(url=call, headers={'User-Agent': AGENT})
        with urlopen(request) as scrapy:
            content = scrapy.read().decode("utf8")
            doc = html.fromstring(content)
            self.price = sanitize_price(safe_element_value(doc.cssselect(self.conf.selector)), brazillian_currency=True)
