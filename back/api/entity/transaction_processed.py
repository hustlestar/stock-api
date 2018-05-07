class TransactionProcessed:
    def __init__(self, transaction_raw):
        self.transaction_raw = transaction_raw

    def __str__(self):
        return self.transaction_raw.date + " " + self.transaction_raw.ticker + " " + self.transaction_raw.direction \
               + " " + str(self.transaction_raw.price)
