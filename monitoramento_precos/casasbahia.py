from requests_xml import XMLSession

from .processor import Processor
from .helpers import sanitize_price, AGENT


class CasasBahia(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        with XMLSession() as session:
            response = session.get(call)
            prices = response.json().get('PrecoProdutos', [])
            if len(prices):
                self.price = prices[0].get('PrecoVenda', {}).get('Preco', 0.0)
