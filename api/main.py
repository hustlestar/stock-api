import os
from datetime import datetime

from api.analytics.report import print_only_interesting, analyze
from api.etl.transform.parsers import get_ticker_list
from api.jobs.stock_list import StockList


def generate_reports(file_list, props, file_prefix):
    for f in file_list:
        tickers = get_ticker_list(f)
        stock_list = StockList(tickers, props)
        for s in stock_list:
            analyze(s)
        interesting_stocks = print_only_interesting(stock_list.stocks, number_of_volume_spikes=3, max_day_range=0.2)
        with open(f.replace(file_prefix, '..\\history\\').replace('.txt', '_' + datetime.now().strftime("%Y-%m-%d") + '.txt'), 'w') as out:
            for s in interesting_stocks:
                out.write(str(s))
        for s in interesting_stocks:
            print s.symbol

def test_report(tickers, props):
    stock_list = StockList(tickers, props)
    for s in stock_list.stocks:
        print s

def read_properties(rel_file_path):
    props = {}
    with open(rel_file_path, 'r') as property_file:
        lines = property_file.readlines()
    for line in lines:
        k, v = line.split('=')
        props[k] = v
    return props

if __name__ == '__main__':
    prefix = '..\\tickers\\under_5\\'
    file_list = [prefix + l for l in os.listdir(prefix)]
    props = read_properties('..\\secrets\\credentials.properties')
    #generate_reports(file_list, props, prefix)
    test_report(['IBM'], props)
