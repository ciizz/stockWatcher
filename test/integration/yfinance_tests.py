import unittest
from model.stock import Stock
from model.watchlist import Watchlist
from model.user import User
from stock_fetcher import get_stock_price


class TestStockFetcher(unittest.TestCase):
    def test_fetch_stock(self):
        tmp1 = get_stock_price("AAPL")
        self.assertEqual(tmp1.get_name(), "Apple Inc.")
        self.assertEqual(tmp1.get_ticker(), "AAPL")
        tmp2 = get_stock_price("GOOG")
        self.assertEqual(tmp2.get_name(), "Alphabet Inc.")
        self.assertEqual(tmp2.get_ticker(), "GOOG")
        tmp3 = get_stock_price("MSFT")
        self.assertEqual(tmp3.get_name(), "Microsoft Corporation")
        self.assertEqual(tmp3.get_ticker(), "MSFT")


