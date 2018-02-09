from no_data_exception import NoDataException

class StockList:
    def __init__(self, tickers, api_key):
        self.tickers = tickers
        self.api_key = api_key
        self.stocks = []

    def analyze_all_stocks(self):
        from main import get_data, parse_stock_json
        for t in self.tickers:
            stock_data = get_data(t, api_key=self.api_key, file_format='json')
            try:
                stock = parse_stock_json(stock_data)
                stock.perfom_full_analysis()
                self.stocks.append(stock)
            except NoDataException:
                print 'No data for {0}'.format(t.upper())

    def full_report(self):
        print 'Full report:'
        for s in self.stocks:
            print s

    def print_only_interesting(self,
                               number_of_volume_spikes=0,
                               change_for_period=0.0,
                               max_day_range=0.0):
        interesting_stocks = []
        for s in self.stocks:
            if s.number_of_volume_spikes >= number_of_volume_spikes \
                    and s.change_for_period >= change_for_period \
                    and s.max_day_range >= max_day_range:
                print s
                interesting_stocks.append(s)
        return interesting_stocks