from monitoramento_precos.engines.viavarejo import ViaVarejo


class Extra(ViaVarejo):
    def __init__(self, conf):
        self.conf = conf
        super().__init__(conf)
