from monitoramento_precos.engines.viavarejo import ViaVarejo


class CasasBahia(ViaVarejo):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
