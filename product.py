class Product:
    def __init__(self, price):
        # self.__price = price if price > 0 else 0
        # self.set_price(price)
        # self.price(price) #not ok here
        self.price = price

    def __str__(self):
        return f"price:{self.__price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(-10)
product.price = 4
print(product.price)
