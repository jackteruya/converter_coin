from src.repository.cripto_info.cripto_info_repository import CriptoInfoAPIRepository
from src.repository.vatcomply_api.coin_api_repository import CoinAPIRepository
from src.service.converter_coin import ConversorCoin


def test_converter_return_float():
    coin_api = CoinAPIRepository()
    cripto_api = CriptoInfoAPIRepository()
    from_ = "usd"
    to_ = "brl"
    value = 5.00
    conversor = ConversorCoin(coin_api, cripto_api)
    conversor.set_from(from_)
    conversor.set_to(to_)
    new_value = conversor.execute(value)
    assert type(new_value.amount_to) is float
    assert new_value.from_ == from_
    assert new_value.to_ == to_
    assert new_value.amount_from == value


def test_converter_to_brl_and_converter_to_usd():
    coin_api = CoinAPIRepository()
    cripto_api = CriptoInfoAPIRepository()

    from_ = "usd"
    to_ = "brl"
    value = 5.00

    conversor = ConversorCoin(coin_api, cripto_api)
    conversor.set_from(from_)
    conversor.set_to(to_)
    new_value = conversor.execute(value)

    conversor.set_from(to_)
    conversor.set_to(from_)
    other_value = conversor.execute(new_value.amount_to)
    assert other_value.amount_to == value
