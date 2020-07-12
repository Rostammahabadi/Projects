from flask import render_template
from app import app
import requests
import pandas as pd

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/stocks/find", methods=["GET"])
def find_stocks():
    return render_template('find_stock.html')

@app.route("/get/stock")
def get_stock():
    resp = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo')
    json_data = resp.json
    data_frame = pd.DataFrame({
    'open':
    })
    import pdb; pdb.set_trace()
    return render_template('stock_data.html', data=json_data)
