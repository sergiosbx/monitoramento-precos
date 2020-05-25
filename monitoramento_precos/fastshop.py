import requests

from .processor import Processor
from .helpers import sanitize_price


class Fastshop(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        result = requests.get(url=call)
        if result.status_code == 200:
            self.price = sanitize_price(result.json().get('priceData', {}).get('offerPriceValue', '0.0'))
