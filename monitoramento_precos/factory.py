from .magalu import Magalu
from .fastshop import Fastshop
from .americanas import Americanas

interface = {
    "FASTSHOP": Fastshop,
    "AMERICANAS": Americanas,
    "MAGALU": Magalu
}


class Factory:
    def __init__(self, conf):
        self.instance = interface[conf.name](conf)

    def fetch_price(self):
        self.instance.fetch_price()

    def compare(self):
        self.instance.compare()

    def notify(self):
        self.instance.notify()

    def update_variation(self):
        self.instance.update_variation()
