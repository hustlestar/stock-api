#!/usr/bin/env python

import os
from datetime import datetime

from analytics.report import get_interesting_stocks, analyze
from etl.transform.parsers import get_ticker_list, parse_alpha_vantage_json_to_stock
from jobs.stock_list import StockList


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


# def test_report(tickers, props):
#     stock_list = StockList(tickers, props)
#     for s in stock_list.stocks:
#         print s
#     interesting_stocks = get_interesting_stocks(stock_list.stocks, number_of_volume_spikes=1, max_day_range=0.2)
#     print interesting_stocks


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


def test_transaction(file_path, props):
    from jobs.transaction_list import TransactionList
    tl = TransactionList(file_path, props)


# def test_plotting(props):
# from api.etl.extract.data_source import get_data_alpha_vantage
# from api.etl.transform.plotting import plot_chart
# stock_data = get_data_alpha_vantage('LHO', props)
# stock_raw = parse_alpha_vantage_json_to_stock(stock_data)
# plot_chart(stock_raw, '..\\charts\\')
# pass

if __name__ == '__main__':
    ticker_dir = '../tickers/under_5/'
    ticker_dir = os.path.normpath(ticker_dir)
    file_list = get_file_list(ticker_dir)
    secrets_path = '../secrets/credentials.properties'
    secrets_path = os.path.normpath(secrets_path)
    props = read_properties(secrets_path)
    # props ={}
    # test_plotting(props)
    generate_reports(file_list, props)
    # test_transaction('..\\transaction\\transaction.log', props)
    # test_report(['CC'], props)
