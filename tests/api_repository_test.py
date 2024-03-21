from src.repository.coins_dto import CoinsDTO
from src.repository.cripto_dto import CriptosDTO
from src.repository.cripto_info.cripto_info_repository import CriptoInfoAPIRepository
from src.repository.vatcomply_api.coin_api_repository import CoinAPIRepository


def test_status_ok_api_coin():
    coin_api = CoinAPIRepository()
    data = coin_api.get_coin()
    assert type(data) is CoinsDTO


def test_status_bad_api_coin():
    coin_api = CoinAPIRepository()
    coin_api._url += "/novo-recurso"
    data = coin_api.get_coin()
    assert data is False


def test_status_ok_api_cripto():
    cripto_api = CriptoInfoAPIRepository()
    data = cripto_api.get_cripto()
    assert type(data) is CriptosDTO


def test_status_bad_api_cripto():
    cripto_api = CriptoInfoAPIRepository()
    cripto_api._url = cripto_api._url[:36] + "novo/"
    data = cripto_api.get_cripto()
    assert data is False
