import unittest
from model.user import User
from model.stock import Stock
from model.watchlist import Watchlist


class TestStock(unittest.TestCase):
    def test_get_name(self):
        tmp = Stock("Apple", "AAPL", 100)
        self.assertEqual(tmp.get_name(), "Apple")

    def test_get_ticker(self):
        tmp = Stock("Apple", "AAPL", 100)
        self.assertEqual(tmp.get_ticker(), "AAPL")

    def test_get_price(self):
        tmp = Stock("Apple", "AAPL", 100)
        self.assertEqual(tmp.get_price(), 100)

    def test_set_price(self):
        tmp = Stock("Apple", "AAPL", 100)
        self.assertEqual(tmp.get_price(), 100)
        tmp.set_price(200)
        self.assertEqual(tmp.get_price(), 200)


if __name__ == '__main__':
    unittest.main()