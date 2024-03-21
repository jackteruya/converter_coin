from dataclasses import dataclass


@dataclass
class DataConverterDTO:
    to_: str
    amount_to: float
    from_: str
    amount_from: float

    def data(self):
        return {
            "from": {str(self.from_).upper(): round(self.amount_from, 7)},
            "to": {str(self.to_).upper(): round(self.amount_to, 7)},
        }
