import unittest
import sys
sys.path.append('../')
from model.user import User
from model.stock import Stock
from model.watchlist import Watchlist

class TestWatchlist(unittest.TestCase):
    def test_add_to_watchlist(self):
        tmp = Watchlist()
        self.assertEqual(tmp.get_stocks(), [])
        stock = Stock("Apple", "AAPL", 100)
        tmp.add_stock(stock)
        self.assertEqual(tmp.get_stocks(), [stock])

    def test_remove_from_watchlist(self):
        tmp = Watchlist()
        stock = Stock("Apple", "AAPL", 100)
        tmp.add_stock(stock)
        self.assertEqual(tmp.get_stocks(), [stock])
        tmp.remove_stock(stock)
        self.assertEqual(tmp.get_stocks(), [])
    
    def test_get_watchlist(self):
        tmp = Watchlist()
        stock = Stock("Apple", "AAPL", 100)
        tmp.add_stock(stock)
        self.assertEqual(tmp.get_stocks(), [stock])


if __name__ == '__main__':
    unittest.main()