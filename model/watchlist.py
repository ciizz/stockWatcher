class Watchlist:
    def __init__(self, name):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def get_stocks(self):
        return self.stocks
