from model.watchlist import Watchlist


class User:
    def __init__(self, user_id):
        self.id = user_id # ip address
        self.watchlist = Watchlist()

    def add_to_watchlist(self, stock):
        self.watchlist.add_stock(stock)

    def remove_from_watchlist(self, stock):
        self.watchlist.remove_stock(stock)

    def get_watchlist(self):
        return self.watchlist
