from ninja.testing import TestClient

from app_api.app.api import router


def test_hello():
    client = TestClient(router)
    response = client.get(path="/hello")

    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_converter():
    client = TestClient(router)
    response = client.get(path="/converter?from_coin=BTC&to_coin=eth&amount=1.0")

    assert response.status_code == 200
    assert type(response.json()) is dict
