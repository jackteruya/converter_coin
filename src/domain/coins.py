class Coins:
    def __init__(self):
        self._usd = 0
        self._brl = 0
        self._eur = 0
        self._btc = 0
        self._eth = 0

    @property
    def usd(self):
        return self._usd

    @usd.setter
    def usd(self, value):
        self._usd = value

    @property
    def brl(self):
        return self._brl

    @brl.setter
    def brl(self, value):
        self._brl = value

    @property
    def eur(self):
        return self._eur

    @eur.setter
    def eur(self, value):
        self._eur = value

    @property
    def btc(self):
        return self._btc

    @btc.setter
    def btc(self, value):
        self._btc = value

    @property
    def eth(self):
        return self._eth

    @eth.setter
    def eth(self, value):
        self._eth = value

    def update_base_coins(self, base):
        # usd_old = self.usd
        # brl_old = self.brl
        # eur_old = self.eur
        # btc_old = self.btc
        # eth_old = self.eth
        old_base = {
            "usd": self.usd,
            "brl": self.brl,
            "eur": self.eur,
            "btc": self.btc,
            "eth": self.eth,
        }
        self.usd = self.usd / old_base[base]
        self.brl = self.brl / old_base[base]
        self.eur = self.eur / old_base[base]
        self.btc = self.btc / old_base[base]
        self.eth = self.eth / old_base[base]
