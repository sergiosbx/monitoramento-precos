from requests_xml import XMLSession

from .processor import Processor
from .viavarejo import ViaVarejo
from .helpers import sanitize_price, AGENT


class PontoFrio(ViaVarejo):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
