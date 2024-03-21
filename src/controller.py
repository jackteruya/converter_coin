from src.repository.cripto_info.cripto_info_repository import CriptoInfoAPIRepository
from src.repository.vatcomply_api.coin_api_repository import CoinAPIRepository
from src.service.converter_coin import ConversorCoin


class ConverterController:
    @staticmethod
    def execute(from_: str, to_: str, amount_: float) -> dict:
        coin_api = CoinAPIRepository()
        cripto_api = CriptoInfoAPIRepository()

        conversor = ConversorCoin(coin_api, cripto_api)
        conversor.set_from(from_)
        conversor.set_to(to_)
        data = conversor.execute(amount_)
        return data.data()
