
from urllib.request import urlopen, Request

from lxml import html

from .b2w import B2w
from .processor import Processor
from .helpers import safe_element_value, sanitize_price, AGENT

class Soubarato(B2w):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
