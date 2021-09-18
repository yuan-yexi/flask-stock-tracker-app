from flask import Blueprint, render_template
import requests
import os

stock = Blueprint('stock', __name__)

API_KEY = os.getenv('STOCK_API_KEY')

def fetch_price(ticker):
    API_URL = f'https://financialmodelingprep.com/api/v3/quote-short/{ticker}?apikey={API_KEY}'
    current_price = requests.get(API_URL).json()

    return current_price[0]["price"]

def fetch_income_statement(ticker):
    API_URL = f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit=12&apikey={API_KEY}"
    income_statement = requests.get(API_URL).json()

    return income_statement

@stock.route("/<string:ticker>")
def quote(ticker):
    price = fetch_price(ticker)

    return render_template("stock/quote.html", ticker=ticker, price=price)

@stock.route('/<string:ticker>/income-statement')
def income_statement(ticker):
    income_statement = fetch_income_statement(ticker)
    chart_labels = [fy["date"] for fy in income_statement if fy["eps"]]
    chart_labels.reverse()
    chart_data = [fy["eps"] for fy in income_statement if fy["eps"]]
    chart_data.reverse()
    chart_params = {
                        "type": "line",
                        "data": {
                            "labels": chart_labels,
                            "datasets": [
                                {"label": "EPS", "data": chart_data}
                            ]
                        }
                    }

    return render_template("stock/income_statement.html", ticker=ticker, income_statement=income_statement, chart_params=chart_params)