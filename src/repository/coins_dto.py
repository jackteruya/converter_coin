from dataclasses import dataclass


@dataclass
class CoinsDTO:
    base: str
    usd: float
    eur: float
    brl: float
