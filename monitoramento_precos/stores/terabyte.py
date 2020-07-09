from monitoramento_precos.engines.scraper import Scraper


class Terabyte(Scraper):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
