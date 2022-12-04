import unittest
from model.user import User
from model.stock import Stock
from model.watchlist import Watchlist

class TestUser(unittest.TestCase):
    def test_add_to_watchlist(self):
        tmp = User("Cesar")
        self.assertEqual(tmp.watchlist.get_stocks(), [])
        stock = Stock("AAPL", "Apple", 100)
        tmp.add_to_watchlist(stock)
        self.assertEqual(tmp.watchlist.get_stocks(), [stock])

    
    def test_remove_from_watchlist(self):
        tmp = User("Cesar")
        stock = Stock("AAPL", "Apple", 100)
        tmp.add_to_watchlist(stock)
        self.assertEqual(tmp.watchlist.get_stocks(), [stock])
        tmp.remove_from_watchlist(stock)
        self.assertEqual(tmp.watchlist.get_stocks(), [])
    
    
    def test_get_watchlist(self):
        tmp = User("Cesar")
        stock = Stock("AAPL", "Apple", 100)
        tmp.add_to_watchlist(stock)
        self.assertEqual(tmp.get_watchlist(), tmp.watchlist)


if __name__ == '__main__':
    unittest.main()