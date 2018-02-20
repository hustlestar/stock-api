from datetime import datetime


class StockRaw(object):
    def __init__(self, ticker, daily_data):
        self.ticker = ticker
        self.daily_data = daily_data

    def __str__(self):
        return self.ticker