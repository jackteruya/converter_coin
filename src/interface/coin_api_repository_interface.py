from abc import ABC, abstractmethod


class CoinApiRepositoryInterface(ABC):
    @abstractmethod
    def get_coin(self, base, date):
        raise NotImplementedError
