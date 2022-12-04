import yfinance as yf
from model.stock import Stock

def get_stock_price(ticker):
    stock_info = yf.Ticker(ticker).info
    stock_name = stock_info["shortName"]
    market_price = stock_info['regularMarketPrice']
    stock = Stock(stock_name, ticker, market_price)
    return stock