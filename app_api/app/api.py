from ninja import Router

from src.controller import ConverterController

router = Router()


@router.get("/hello")
def hello(request):
    return {"msg": "Hello World"}


@router.get("/converter")
def converter(request, from_coin: str, to_coin: str, amount: float):
    return ConverterController.execute(from_coin, to_coin, amount)
