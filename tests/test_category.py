def test_category(category_one, category_two):
    assert category_one.name == "Телефоны"
    assert category_one.description == "Телефон на каждый день"
    assert len(category_one.products_list) == 2

    assert category_two.count_category == 2
    assert category_two.count_product == 2


def test_category_get_product_property(category_one):
    assert category_one.get_product == "Samsung, 80000.0 руб. Остаток: 10 шт.Iphone, 125000.0 руб. Остаток: 5 шт."


def test_category_get_product_setter(category_one, product):
    assert len(category_one.products_list) == 2
    category_one.get_product = product
    assert len(category_one.products_list) == 3
