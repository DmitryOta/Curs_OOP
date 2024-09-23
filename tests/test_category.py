def test_category(category_one, category_two):
    assert category_one.name == "Телефоны"
    assert category_one.description == "Телефон на каждый день"
    assert len(category_one.products) == 2

    assert category_two.count_category == 2
    assert category_two.count_product == 2