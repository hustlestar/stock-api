import json

from api.entity.stock_raw import StockRaw
from api.entity.stock_day import DailyData
from api.etl.transform.no_data_exception import NoDataException


def parse_json_to_stock(json_string):
    json_map = json.loads(json_string)
    try:
        meta_data_map = json_map[u'Meta Data']
        symbol = meta_data_map[u'2. Symbol']
        print symbol

        last_update = meta_data_map[u'3. Last Refreshed']
        print last_update

        daily_time_series_map = json_map[u'Time Series (Daily)']

        _dates = daily_time_series_map.keys()
        sorted_dates = sorted(_dates, reverse=True)
        daily_data = []
        for date in sorted_dates:
            day_map = daily_time_series_map[date]
            open_ = float(day_map[u'1. open'])
            high_ = float(day_map[u'2. high'])
            low_ = float(day_map[u'3. low'])
            close_ = float(day_map[u'4. close'])
            volume_ = int(day_map[u'5. volume'])
            new_day = DailyData(date, open_, high_, low_, close_, volume_)
            daily_data.append(new_day)
    except KeyError:
        raise NoDataException()

    return StockRaw(symbol, daily_data)


def get_ticker_list(file_name):
    tickers = []
    with open(file_name) as raw:
        data = raw.readlines()
        for l in data:
            ar = l.split(' ')
            tickers += [a for a in ar if len(a) > 0]
    return tickers