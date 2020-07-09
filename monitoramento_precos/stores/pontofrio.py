from monitoramento_precos.engines.viavarejo import ViaVarejo


class PontoFrio(ViaVarejo):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
