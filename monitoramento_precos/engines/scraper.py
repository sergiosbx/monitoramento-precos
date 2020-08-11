
from urllib.request import urlopen, Request

from lxml import html

from monitoramento_precos.processor import Processor
from monitoramento_precos.helpers import safe_element_value, sanitize_price, AGENT


class Scraper(Processor):
    def __init__(self, conf, brazillian_currency=True):
        self.conf = conf
        self.brazillian_currency = brazillian_currency
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        request = Request(url=call, headers={'User-Agent': AGENT})
        with urlopen(request, timeout=20) as scrapy:
            charset = scrapy.headers.get_content_charset()
            content = scrapy.read().decode(charset or 'utf-8')
            doc = html.fromstring(content)
            tracer = getattr(doc, self.conf.selector_type)
            price = safe_element_value(tracer(self.conf.selector))
            self.price = sanitize_price(price=price, brazillian_currency=self.brazillian_currency)
