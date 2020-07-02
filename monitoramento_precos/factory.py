from .magalu import Magalu
from .fastshop import Fastshop
from .americanas import Americanas
from .casasbahia import CasasBahia

from .helpers import get_logger

logger = get_logger()

interface = {
    "FASTSHOP": Fastshop,
    "AMERICANAS": Americanas,
    "MAGALU": Magalu,
    "CASASBAHIA": CasasBahia
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
