class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
