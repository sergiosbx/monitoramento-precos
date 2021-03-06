from requests_xml import XMLSession

from monitoramento_precos.processor import Processor


class ViaVarejo(Processor):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)

    def fetch_price(self):
        call = self.conf.api.format(api_product_code=self.conf.api_product_code)
        with XMLSession() as session:
            response = session.get(call, timeout=20)
            prices = response.json().get('PrecoProdutos', [])
            if len(prices):
                self.price = prices[0].get('PrecoVenda', {}).get('Preco', 0.0)
