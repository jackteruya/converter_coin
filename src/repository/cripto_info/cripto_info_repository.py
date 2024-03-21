import requests

from src.interface.cripto_api_repository_interface import CriptoApiRepositoryInterface
from src.repository.cripto_dto import CriptosDTO

info_api = (
    "https://api.infomoney.com.br/crypto/high-low?"
    "orderAtributte=Volume&pageIndex=1&pageSize=5&search=&type=json"
)


class CriptoInfoAPIRepository(CriptoApiRepositoryInterface):
    def __init__(self):
        self._url = info_api
        self._requests = requests
        self._base_coin = "BRL"
        self.criptos = ["BTC", "ETH"]

    def get_cripto(self):
        response = self._requests.get(url=self._url, headers=self.get_header())
        if response.status_code != 200:
            return False
        criptos = {
            data["StockCode"]: str(data["ValueFormatted"])
            .replace(".", "")
            .replace(",", ".")
            for data in response.json()["Data"]
            if data["StockCode"] in self.criptos
        }
        return CriptosDTO(
            base=self._base_coin,
            btc=float(criptos[self.criptos[0]]),
            eth=float(criptos[self.criptos[1]]),
        )

    def get_header(self):
        headers = {
            "Content-Type": "application/json",
        }

        return headers
