from ninja import NinjaAPI

from src.controller import ConverterController

api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/converter")
def converter(request, from_coin: str, to_coin: str, amount: float):
    return ConverterController.execute(from_coin, to_coin, amount)
