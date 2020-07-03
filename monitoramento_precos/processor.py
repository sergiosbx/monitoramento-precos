import logging
from abc import ABC, abstractmethod

from .dao import Dao
from .compare import Compare
from .helpers import safe_float, get_logger

logger = get_logger()


class Processor(ABC):
    def __init__(self, conf):
        self.accomplished = None
        self.price = None
        self.conf = conf

    @abstractmethod
    def fetch_price(self):
        pass

    def compare(self):
        if self.price:
            self.accomplished = Compare(self.conf, self.price).execute()

    def update_variation(self):
        if self.price and safe_float(self.price) != safe_float(self.conf.last_price):
            logger.info(f"[{self.conf.name}] ({self.conf.description}) :: {self.conf.last_price} -> {self.price}")
            Dao().insert_price_varation(self.conf.stores_products_id, self.price)

    def notify(self):
        if self.accomplished:
            print(self.accomplished)
