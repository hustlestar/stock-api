class TransactionRaw(object):
    def __init__(self, date, ticker, direction, price):
        self.date = date
        self.ticker = ticker
        self.direction = direction
        self.price = float(price)
