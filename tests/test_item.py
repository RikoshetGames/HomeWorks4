"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest


def test_init():
    item = Item("Смартфон", 10000, 5)
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 5


@pytest.fixture
def test_class_item():
    return Item("Ноутбук", 15000, 5)

def test_calculate_total_price(test_class_item):
    """
    При создании экземляр класса с определенной ценой
    и количеством, должно вернутся произведение этих чисел.
    """
    assert test_class_item.calculate_total_price() == 75000


def test_apply_discount(test_class_item):
    """При создании экземпляра класса с определенной ценой, должна вернуться цена с учетом скидки"""
    Item.pay_rate = 0.8
    assert test_class_item.apply_discount() == 12000
    assert test_class_item.price == 12000


def test_add():
    assert Item("iPhone 14", 120000, 5) + Item("iPhone 14", 120000, 5) == 10



def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'
    assert item.name != 'Смартфон'


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == 'Смартфон'
