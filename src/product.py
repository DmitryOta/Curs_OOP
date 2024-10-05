class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_dict):
        product_list = []
        for key, velue in product_dict.items():
            product_list.append(velue)
        return cls(*product_list)

    @property
    def price_int(self):
        return self.__price

    @property
    def price(self):
        return f"{self.__price}"

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            self.__price = price
