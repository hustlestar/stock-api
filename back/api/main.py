#!/usr/bin/env python

import os

from etl.transform.parsers import parse_alpha_vantage_json_to_stock
from utils import read_properties, get_file_list, generate_reports


# def test_report(tickers, props):
#     stock_list = StockList(tickers, props)
#     for s in stock_list.stocks:
#         print s
#     interesting_stocks = get_interesting_stocks(stock_list.stocks, number_of_volume_spikes=1, max_day_range=0.2)
#     print interesting_stocks


def test_transaction(file_path, props):
    from jobs.transaction_list import TransactionList
    tl = TransactionList(file_path, props)


def test_plotting(props):
    from etl.extract.data_source import get_data_alpha_vantage
    from etl.transform.plotting import plot_chart
    stock_data = get_data_alpha_vantage('LHO', props)
    stock_raw = parse_alpha_vantage_json_to_stock(stock_data)
    return plot_chart(stock_raw, '../charts/')


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
