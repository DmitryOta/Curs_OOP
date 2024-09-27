import pytest

from src.category import Category
from src.product import Product
from src.product_search import ProductSearch


@pytest.fixture
def category_one():
    return Category(
        name="Телефоны",
        description="Телефон на каждый день",
        products=[
            Product(name="Samsung", description="Цвет черный", price=80000.0, quantity=10),
            Product(name="Iphone", description="Цвет белый", price=125000.0, quantity=5),
        ],
    )


@pytest.fixture
def category_two():
    return Category(
        name="Планшеты",
        description="Уже не телефон, но еще не ноутбук",
        products=[
            Product(name="Samsung", description="Цвет зеленый", price=45000.0, quantity=15),
            Product(name="Ipad", description="Цвет серый", price=100000.0, quantity=3),
        ],
    )


@pytest.fixture
def product():
    return Product(name="Ipad", description="Цвет серый", price=100000.0, quantity=3)


@pytest.fixture
def product_one():
    return Product(name="Ipad Mini", description="Цвет серый", price=90000.0, quantity=7)


@pytest.fixture
def product_two():
    return Product(name="Ipad Pro", description="Цвет черный", price=150000.0, quantity=10)


@pytest.fixture
def category_iterator(category_one):
    return ProductSearch(category_one)
