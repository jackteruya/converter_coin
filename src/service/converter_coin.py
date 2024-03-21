from src.domain.coins import Coins
from src.interface.coin_api_repository_interface import CoinApiRepositoryInterface
from src.interface.cripto_api_repository_interface import CriptoApiRepositoryInterface
from src.service.data_converter_dto import DataConverterDTO


class ConversorCoin:
    def __init__(
        self,
        coins_api_repository: CoinApiRepositoryInterface,
        criptos_api_repository: CriptoApiRepositoryInterface,
    ):
        self._coin_api = coins_api_repository
        self._cripto_api = criptos_api_repository
        self._from = None
        self._to = None

    def execute(self, amount: float):
        if self.validation_param():
            return "Error: the to and from parameters are required"
        coin = self.treat_data(self._from)
        return DataConverterDTO(
            from_=self._from,
            amount_from=amount,
            to_=self._to,
            amount_to=amount * coin.__getattribute__(self._to),
        )

    def set_from(self, value: str):
        self._from = value

    def set_to(self, value: str):
        self._to = value

    def validation_param(self):
        if self._from is None or self._to is None:
            return False

    def get_data_coins(self, base: str = "USD", date=None):
        return self._coin_api.get_coin(base, date)

    def get_data_criptos(self):
        return self._cripto_api.get_cripto()

    def treat_data(self, base_coin: str):
        base_coin = str(base_coin).lower()
        coin_api = self.get_data_coins()
        cripto_api = self.get_data_criptos()
        coin = Coins()
        coin.usd = coin_api.usd
        coin.brl = coin_api.brl
        coin.eur = coin_api.eur
        coin.btc = coin_api.__getattribute__(str(coin_api.base).lower()) / (
            cripto_api.btc / coin_api.__getattribute__(str(cripto_api.base).lower())
        )
        coin.eth = coin_api.__getattribute__(str(coin_api.base).lower()) / (
            cripto_api.eth / coin_api.__getattribute__(str(cripto_api.base).lower())
        )
        if coin.__getattribute__(base_coin) != 1.0:
            coin.update_base_coins(base_coin)
        return coin
