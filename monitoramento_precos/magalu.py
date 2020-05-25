import requests

from .processor import Processor


class Magalu(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        result = requests.get(url=call, headers={'Authorization': self.conf.token})
        if result.status_code == 200:
            self.price = result.json().get('data', {}).get('price', 0.0)
