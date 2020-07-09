
from monitoramento_precos.engines.scraper import Scraper


class FallenStore(Scraper):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
