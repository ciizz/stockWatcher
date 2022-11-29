from model.watchlist import Watchlist


class User:
    def __init__(self):
        self.watchlist = Watchlist();

    def add_to_watchlist(self, stock):
        self.watchlist.append(stock)

    def remove_from_watchlist(self, stock):
        self.watchlist.remove(stock)

    def get_watchlist(self):
        return self.watchlist
