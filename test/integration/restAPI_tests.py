import unittest
import requests
from app import stocks_to_list
from model.stock import Stock
from model.watchlist import Watchlist
from model.user import User
from stock_fetcher import get_stock_price

url = 'https://ecse437-stockwatcher.herokuapp.com/'

class TestRestAPI(unittest.TestCase):
    def test_get_stock(self):
        ticker = "AAPL"
        stock = get_stock_price(ticker)
        response = requests.get(url + "stock/" + ticker)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ticker"], stock.ticker)
        self.assertEqual(response.json()["name"], stock.name)
        ticker = "GOOG"
        stock = get_stock_price(ticker)
        response = requests.get(url + "stock/" + ticker)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ticker"], stock.ticker)
        self.assertEqual(response.json()["name"], stock.name)
        ticker = "MSFT"
        stock = get_stock_price(ticker)
        response = requests.get(url + "stock/" + ticker)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ticker"], stock.ticker)
        self.assertEqual(response.json()["name"], stock.name)
    
    def test_get_watchlist(self):
        tmp_user = User("127.0.0.7")
        response = requests.get(url + "get_watchlist")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), stocks_to_list(tmp_user.get_watchlist().get_stocks()))
        
    def test_add_to_watchlist(self):
        tmp_user = User("127.0.0.7")
        ticker = "AAPL"
        stock = get_stock_price(ticker)
        tmp_user.add_to_watchlist(stock)
        response = requests.put(url + "add_to_watchlist/" + ticker)
        self.assertEqual(response.status_code, 200)

    def test_remove_from_watchlist(self):
        tmp_user = User("127.0.0.7")
        ticker = "AAPL"
        stock = get_stock_price(ticker)
        tmp_user.remove_from_watchlist(stock)
        response = requests.put(url + "remove_from_watchlist/" + ticker)
        self.assertEqual(response.status_code, 200)