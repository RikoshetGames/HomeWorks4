"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest

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