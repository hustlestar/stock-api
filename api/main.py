import os
from datetime import datetime

from api.analytics.report import get_interesting_stocks, analyze
from api.etl.transform.parsers import get_ticker_list
from api.jobs.stock_list import StockList


def generate_reports(file_list, props, file_prefix):
    for f in file_list:
        tickers = get_ticker_list(f)
        stock_list = StockList(tickers, props)
        # for s in stock_list.stocks:
        #     analyze(s)
        interesting_stocks = get_interesting_stocks(stock_list.stocks, number_of_volume_spikes=3, max_day_range=0.2)
        with open(f.replace(file_prefix, '..\\history\\').replace('.txt', '_' + datetime.now().strftime("%Y-%m-%d") + '.txt'), 'w') as out:
            for s in interesting_stocks:
                out.write(str(s))
        for s in interesting_stocks:
            print s.stock_raw.symbol


def test_report(tickers, props):
    stock_list = StockList(tickers, props)
    for s in stock_list.stocks:
        print s
    interesting_stocks = get_interesting_stocks(stock_list.stocks, number_of_volume_spikes=1, max_day_range=0.2)
    print interesting_stocks


def read_properties(rel_file_path):
    props = {}
    with open(rel_file_path, 'r') as property_file:
        lines = property_file.readlines()
    for line in lines:
        k, v = line.split('=')
        props[k] = v.strip()
    return props


def get_file_list(ticker_dir, skip_file=None):
    file_list = [ticker_dir + l for l in os.listdir(ticker_dir) if l != skip_file]
    return file_list

def test_transaction(file_path, props):
    from api.jobs.transaction_list import TransactionList
    tl = TransactionList(file_path, props)

if __name__ == '__main__':
    ticker_dir = '..\\tickers\\under_5\\'
    file_list = get_file_list(ticker_dir, skip_file="basic_materials_under_5.txt")
    props = read_properties('..\\secrets\\credentials.properties')
    #generate_reports(file_list, props, ticker_dir)
    test_transaction('..\\transaction\\transaction.log', props)
    # test_report(['CC'], props)
