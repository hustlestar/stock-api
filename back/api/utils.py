import os
from datetime import datetime

from analytics.report import get_interesting_stocks
from etl.transform.parsers import get_ticker_list
from jobs.stock_list import StockList


def read_properties(rel_file_path):
    props = {}
    with open(rel_file_path, 'r') as property_file:
        lines = property_file.readlines()
    for line in lines:
        k, v = line.split('=')
        props[k] = v.strip()
    return props


def get_file_list(ticker_dir, skip_file=None):
    file_list = [os.path.join(ticker_dir, file_name) for file_name in os.listdir(ticker_dir) if file_name != skip_file]
    return file_list


def generate_reports(file_list, props):
    history_dir = os.path.normpath('../history/')
    if not os.path.exists(history_dir):
        os.mkdir(history_dir)
    history_day_dir = os.path.normpath(os.path.join(history_dir, datetime.now().strftime("%Y-%m-%d")))
    if not os.path.exists(history_day_dir):
        os.mkdir(history_day_dir)
    for f in file_list:
        tickers = get_ticker_list(f)
        file_name = os.path.basename(f)
        stock_list = StockList(tickers, props)
        # for stock in stock_list.stocks:
        #     analyze(stock)
        interesting_stocks = get_interesting_stocks(stock_list.stocks_processed,
                                                    number_of_volume_spikes=3,
                                                    max_day_range=0.2)
        replace_with = '_' + datetime.now().strftime("%Y-%m-%d") + '.txt'
        with open(os.path.join(history_day_dir, file_name).replace('.txt', replace_with), 'w') as out:
            for stock in interesting_stocks:
                out.write(str(stock))
        for stock in interesting_stocks:
            print stock.stock_raw.ticker