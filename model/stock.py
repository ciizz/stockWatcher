class Stock:
    def __init__(self, name, ticker, price):
        self.name = name
        self.ticker = ticker
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"

    def get_name(self):
        return self.name
        
    def get_ticker(self):
        return self.ticker

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
