import os

from flask import Flask, url_for, render_template, Markup
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/plot')
def get_ticker():
    secrets_path = '../secrets/credentials.properties'
    secrets_path = os.path.normpath(secrets_path)
    props = utils.read_properties(secrets_path)

    stock_raw =  utils.get_stock_raw('AAPL', props)
    chart_div = utils.get_chart_for(stock_raw, props)

    return render_template("ticker.html", chart=Markup(chart_div))

if __name__ == '__main__':
    app.run(debug=True)