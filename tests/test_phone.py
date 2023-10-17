from src.phone import Phone
import pytest

def test_init():
    phone = Phone("Xiaomi 12", 30000, 5, 2)
    assert phone.name == "Xiaomi 12"
    assert phone.price == 30000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr():
    phone = Phone("Xiaomi 12", 30000, 5, 2)
    assert repr(phone) == "Phone('Xiaomi 12', 30000, 5, 2)"


def test_str():
    phone = Phone("Xiaomi 12", 30000, 5, 2)
    assert str(phone) == "Xiaomi 12"


def test_number_of_sim():
    phone = Phone("Xiaomi 12", 30000, 5, 2)
    assert phone.number_of_sim == 2