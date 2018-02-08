import json
import urllib2
from datetime import datetime

from stock import Stock
from stock_day import DailyData
from stock_list import StockList
from no_data_exception import NoDataException


def get_data(ticker, api_key, file_format='csv'):
    url = "https://www.alphavantage.co/query?" + \
          "function=TIME_SERIES_DAILY&" + \
          "symbol={0}&".format(ticker) + \
          "datatype={0}&".format(file_format) + \
          "apikey={0}".format(api_key)
    response = urllib2.urlopen(url)

    html = response.read()
    # print html
    return html


def parse_stock_json(json_string):
    parsed_dict = json.loads(json_string)
    try:
        meta_data = parsed_dict[u'Meta Data']
        symbol = meta_data[u'2. Symbol']
        print symbol
        last_update = meta_data[u'3. Last Refreshed']
        print last_update
        daily_time_series = parsed_dict[u'Time Series (Daily)']

        _dates = daily_time_series.keys()
        sorted_dates = sorted(_dates, reverse=True)
        daily_data = []
        for date in sorted_dates:
            day_data = daily_time_series[date]
            open_ = float(day_data[u'1. open'])
            high_ = float(day_data[u'2. high'])
            low_ = float(day_data[u'3. low'])
            close_ = float(day_data[u'4. close'])
            volume_ = int(day_data[u'5. volume'])
            new_data = DailyData(date, open_, high_, low_, close_, volume_)
            daily_data.append(new_data)
    except KeyError:
        raise NoDataException()

    return Stock(symbol, daily_data)


def parse_tickers(file_name):
    tickers = []
    with open(file_name) as raw:
        data = raw.readlines()
        for l in data:
            ar = l.split(' ')
            tickers += [a for a in ar if len(a) > 0]
    return tickers


def generate_reports(file_list, api_key):
    for f in file_list:
        tickers = parse_tickers(f)
        stock_list = StockList(tickers, api_key)
        stock_list.analyze_all_stocks()
        interesting_stocks = stock_list.print_only_interesting(number_of_volume_spikes=3, max_day_range=0.2)
        with open(f.replace('.txt', '_' + datetime.now().strftime("%Y-%m-%d") + '.txt'), 'w') as out:
            for s in interesting_stocks:
                out.write(str(s))
        for s in interesting_stocks:
            print s.symbol


if __name__ == '__main__':
    file_list = ['healthcare_under_5.txt']
    generate_reports(file_list, 'RWOH7RVGZIFSZK4X')
