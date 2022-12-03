from flask import Flask, jsonify, request
from model.user import User
from model.watchlist import Watchlist
from model.stock import Stock
from stock_fetcher import get_stock_price

app = Flask(__name__)

user_hashmap = {}

# get stock
@app.route("/stock/<ticker>")
def get_stock(ticker):
    stock = get_stock_price(ticker)
    return jsonify(stock.__dict__)

@app.route("/get_watchlist", methods=["GET"])
def get_watchlist():
    user_IP = request.remote_addr
    tmp_user = None
    if user_IP in user_hashmap:
        tmp_user = user_hashmap[user_IP]
    else:
        tmp_user = User(user_IP)
        user_hashmap[user_IP] = tmp_user
    return jsonify(stocks_to_list(tmp_user.get_watchlist().get_stocks()))


@app.route("/add_to_watchlist/<ticker>", methods=["PUT"])
def add_to_watchlist(ticker):
    user_IP = request.remote_addr
    tmp_user = None
    if user_IP in user_hashmap:
        tmp_user = user_hashmap[user_IP]
    else:
        tmp_user = User(user_IP)
        user_hashmap[user_IP] = tmp_user
    stock = get_stock_price(ticker)
    tmp_user.add_to_watchlist(stock)
    return jsonify(stocks_to_list(tmp_user.get_watchlist().get_stocks()))


@app.route("/remove_from_watchlist/<ticker>", methods=["PUT"])
def remove_from_watchlistticker(ticker):
    user_IP = request.remote_addr
    tmp_user = None
    if user_IP in user_hashmap:
        tmp_user = user_hashmap[user_IP]
    else:
        tmp_user = User(user_IP)
        user_hashmap[user_IP] = tmp_user
    stock = get_stock_price(ticker)
    tmp_user.remove_from_watchlist(stock)
    return jsonify(stocks_to_list(tmp_user.get_watchlist().get_stocks()))


# helper method
def stocks_to_list(stocks):
    if stocks is None:
        return None
    stock_list = []
    for stock in stocks:
        stock_list.append(stock.__dict__)
    return stock_list