from abc import ABC, abstractmethod

from .dao import Dao
from .compare import Compare
from .mailsender import MailSender
from .helpers import safe_float, get_logger

logger = get_logger()


class Processor(ABC):
    def __init__(self, conf):
        self.accomplished = None
        self.price = None
        self.conf = conf
        self.dao = Dao()
        if self.conf.last_price:
            self.conf.last_price = safe_float(self.conf.last_price)

    @abstractmethod
    def fetch_price(self):
        pass

    def compare(self):
        if self.price:
            self.accomplished = Compare(self.conf, self.price).execute()

    def update_variation(self):
        if self.price and safe_float(self.price) != safe_float(self.conf.last_price):
            logger.info(f"[{self.conf.name}] ({self.conf.description}) :: {self.conf.last_price} -> {self.price}")
            self.dao.insert_price_varation(self.conf.stores_products_id, self.price)

    def notify(self):
        if self.accomplished:
            sender = MailSender(receiver=self.conf.email)
            sender.with_message(description=self.conf.description, price=self.price,
                                last_price=self.conf.last_price, anchor=self.conf.anchor)
            sender.send()
            self.dao.remove_user_monitoring(email=self.conf.email, product_id=self.conf.product_id)
