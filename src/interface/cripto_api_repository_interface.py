from abc import ABC, abstractmethod


class CriptoApiRepositoryInterface(ABC):
    @abstractmethod
    def get_cripto(self):
        raise NotImplementedError
