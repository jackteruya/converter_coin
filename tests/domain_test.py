from src.domain.coins import Coins


coins_base_usd = {
    "base": "usd",
    "usd": 1.0,
    "brl": 5.01789,
    "eur": 0.92216,
    "btc": 0.000014936508031,
    "eth": 0.000283998501306,
}

coins_base_eur = {
    "base": "eur",
    "usd": 1.08441051444435,
    "brl": 5.44145267632515,
    "eur": 1.0,
    "btc": 0.000016197306358,
    "eth": 0.000307970960903,
}

coins_base_brl = {
    "base": "brl",
    "usd": 0.19928695128829,
    "brl": 1.0,
    "eur": 0.18377445500001,
    "btc": 0.000002976651148,
    "eth": 0.000056597195496,
}


def test_create_coins():
    coins = Coins()
    coins.usd = coins_base_usd["usd"]
    coins.brl = coins_base_usd["brl"]
    coins.eur = coins_base_usd["eur"]
    coins.btc = coins_base_usd["btc"]
    coins.eth = coins_base_usd["eth"]

    assert coins.usd == coins_base_usd["usd"]
    assert coins.brl == coins_base_usd["brl"]
    assert coins.eur == coins_base_usd["eur"]
    assert coins.btc == coins_base_usd["btc"]
    assert coins.eth == coins_base_usd["eth"]


def test_update_base_coin_to_eur():
    coins = Coins()
    coins.usd = coins_base_usd["usd"]
    coins.brl = coins_base_usd["brl"]
    coins.eur = coins_base_usd["eur"]
    coins.btc = coins_base_usd["btc"]
    coins.eth = coins_base_usd["eth"]

    coins.update_base_coins(coins_base_eur["base"])

    assert round(coins.usd, 5) == round(coins_base_eur["usd"], 5)
    assert round(coins.brl, 5) == round(coins_base_eur["brl"], 5)
    assert round(coins.eur, 5) == round(coins_base_eur["eur"], 5)
    assert round(coins.btc, 5) == round(coins_base_eur["btc"], 5)
    assert round(coins.eth, 5) == round(coins_base_eur["eth"], 5)


def test_update_base_coin_to_brl():
    coins = Coins()
    coins.usd = coins_base_usd["usd"]
    coins.brl = coins_base_usd["brl"]
    coins.eur = coins_base_usd["eur"]
    coins.btc = coins_base_usd["btc"]
    coins.eth = coins_base_usd["eth"]

    coins.update_base_coins(coins_base_brl["base"])

    assert round(coins.usd, 5) == round(coins_base_brl["usd"], 5)
    assert round(coins.brl, 5) == round(coins_base_brl["brl"], 5)
    assert round(coins.eur, 5) == round(coins_base_brl["eur"], 5)
    assert round(coins.btc, 5) == round(coins_base_brl["btc"], 5)
    assert round(coins.eth, 5) == round(coins_base_brl["eth"], 5)
