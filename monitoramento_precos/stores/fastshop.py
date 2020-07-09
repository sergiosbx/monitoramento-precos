import requests

from monitoramento_precos.processor import Processor
from monitoramento_precos.helpers import sanitize_price


class Fastshop(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        result = requests.get(url=call)
        if result.status_code == 200:
            price = result.json().get('priceData', {}).get('offerPriceValue', '0.0')
            self.price = sanitize_price(price=price, brazillian_currency=False)
