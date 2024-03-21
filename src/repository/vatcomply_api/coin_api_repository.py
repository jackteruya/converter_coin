import requests

from src.interface.coin_api_repository_interface import CoinApiRepositoryInterface
from src.repository.coins_dto import CoinsDTO


class CoinAPIRepository(CoinApiRepositoryInterface):
    def __init__(self):
        self._url = "https://api.vatcomply.com/rates"
        self._requests = requests
        self._base_coin = "USD"
        self.coins = ["USD", "EUR", "BRL"]

    def get_coin(self, base="USD", date=None):
        url = f"{self._url}?base={base}"
        if date:
            url += f"&date={date}"
        response = self._requests.get(url=url, headers=self.get_header())
        if response.status_code != 200:
            return False
        coins_result = response.json()["rates"]
        return CoinsDTO(
            base=base,
            usd=coins_result[self.coins[0]],
            eur=coins_result[self.coins[1]],
            brl=coins_result[self.coins[2]],
        )

    def get_header(self):
        headers = {
            "Content-Type": "application/json",
        }

        return headers
