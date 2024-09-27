from src.category import Category
from src.product import Product


class ProductSearch:

    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products.products_list):
            product = self.products.products_list[self.index]
            self.index += 1
            return product
        raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductSearch(category1)
    for categor in iterator:
        print(categor)
    print("lol")
    for categor in iterator:
        print(categor)
