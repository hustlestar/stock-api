from datetime import datetime


class StockRaw(object):
    def __init__(self, symbol, daily_data):
        self.symbol = symbol
        self.daily_data = daily_data

    def __str__(self):
        return self.symbol