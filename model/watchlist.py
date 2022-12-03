class Watchlist:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        # remove stock with same name and ticker
        for i in range(len(self.stocks)):
            if self.stocks[i].get_ticker() == stock.get_ticker():
                self.stocks.pop(i)
                break

    def get_stocks(self):
        return self.stocks
