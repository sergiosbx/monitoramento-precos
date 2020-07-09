from .stores.extra import Extra
from .stores.kabum import Kabum
from .stores.magalu import Magalu
from .stores.pichau import Pichau
from .stores.fastshop import Fastshop
from .stores.shoptime import Shoptime
from .stores.terabyte import Terabyte
from .stores.carrefour import Carrefour
from .stores.pontofrio import PontoFrio
from .stores.soubarato import Soubarato
from .stores.submarino import Submarino
from .stores.americanas import Americanas
from .stores.casasbahia import CasasBahia
from .stores.fallenstore import FallenStore

from .helpers import get_logger

logger = get_logger()

interface = {
    "FASTSHOP": Fastshop,
    "AMERICANAS": Americanas,
    "SHOPTIME": Shoptime,
    "MAGALU": Magalu,
    "CASASBAHIA": CasasBahia,
    "EXTRA": Extra,
    "PONTOFRIO": PontoFrio,
    "SUBMARINO": Submarino,
    "SOUBARATO": Soubarato,
    "CARREFOUR": Carrefour,
    "TERABYTE": Terabyte,
    "KABUM": Kabum,
    "PICHAU": Pichau,
    "FALLENSTORE": FallenStore,
}


class Factory:
    def __init__(self, conf):
        self.instance = interface[conf.name](conf)

    def fetch_price(self):
        try:
            self.instance.fetch_price()
        except Exception as exc:
            logger.warning(f'Error on fetch price for {type(self.instance).__name__}: {exc}')

    def compare(self):
        self.instance.compare()

    def notify(self):
        try:
            self.instance.notify()
        except Exception as exc:
            logger.warning(f'Error on notify price - {type(self.instance).__name__}: {exc}')

    def update_variation(self):
        try:
            self.instance.update_variation()
        except Exception as exc:
            logger.warning(f'Error on update variation - {type(self.instance).__name__}: {exc}')
