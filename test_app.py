"""Testes unitários e de contrato HTTP para o laboratório."""
import pytest
from app import calculate_shipping, create_app


def test_calculate_shipping_with_string_rate():
    assert calculate_shipping(100.0, "5.50") == pytest.approx(105.5)


@pytest.mark.parametrize("base,tax,expected", [
    (0.0, "0", 0.0),
    (10.0, "2.5", 12.5),
    (19.9, "0.10", 20.0),
])
def test_calculate_shipping_cases(base, tax, expected):
    assert calculate_shipping(base, tax) == pytest.approx(expected)


def test_shipping_endpoint():
    pytest.importorskip("flask")
    client = create_app().test_client()
    response = client.post("/shipping", json={"price": 100.0, "tax": "5.50"})
    assert response.status_code == 200
    assert response.get_json() == {"total": 105.5}


def test_invalid_payload():
    pytest.importorskip("flask")
    client = create_app().test_client()
    response = client.post("/shipping", json={"tax": "5.50"})
    assert response.status_code == 400
