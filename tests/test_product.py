from src.product import Product


def test_product(product):
    assert product.name == "Ipad"
    assert product.description == "Цвет серый"
    assert product.price_int == 100000.0
    assert product.quantity == 3


def test_product_create():
    product = Product("Samsung S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.name = "Samsung S23 Ultra"
    product.description = "256GB, Серый цвет, 200MP камера"
    product.price = 180000.0
    product.quantity = 5


def test_price_setter(capsys, product):
    product.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product):
    assert str(product) == "Ipad, 100000.0 руб. Остаток: 3 шт."


def test_product_add(product_one, product_two):
    assert product_one + product_two == 2130000.0
