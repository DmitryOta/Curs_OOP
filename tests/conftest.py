import pytest


from  src.product import Product
from  src.category import Category


@pytest.fixture
def category_one():
    return Category(
        name="Телефоны",
        description="Телефон на каждый день",
        products=[
            Product(name="Samsung", description="Цвет черный", price=80000.0, quantity=10),
            Product(name="Iphone", description="Цвет белый", price=125000.0, quantity=5),
        ]
    )


@pytest.fixture
def category_two():
    return Category(
        name="Планшеты",
        description="Уже не телефон, но еще не ноутбук",
        products=[
            Product(name="Samsung", description="Цвет зеленый", price=45000.0, quantity=15),
            Product(name="Ipad", description="Цвет серый", price=100000.0, quantity=3),
        ]
    )


@pytest.fixture
def product():
    return Product(name="Ipad", description="Цвет серый", price=100000.0, quantity=3)
