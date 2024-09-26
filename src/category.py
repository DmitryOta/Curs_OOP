from src.product import Product


class Category:
    name: str
    description: str
    products: list

    count_category = 0
    count_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.count_category += 1
        Category.count_product += 1

    def add_product(self, products):
        self.__products.append(products)
        Category.count_category += 1

    @property
    def products(self):
        return f"{self.__products}"

    @property
    def products_list(self):
        return self.__products

    @property
    def get_product(self):
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return str_product

    @get_product.setter
    def get_product(self, product: Product):
        self.__products.append(product)
        Category.count_product += 1
