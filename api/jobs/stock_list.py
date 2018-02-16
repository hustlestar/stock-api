from api.etl.extract.data_source import get_data_via_http
from api.etl.transform.no_data_exception import NoDataException
from api.etl.transform.parsers import parse_json_to_stock


class StockList:
    def __init__(self, tickers, props):
        self.tickers = tickers
        self.stocks = []
        self.api_key = props.get('api.key')
        self._get_data_for_tickers()

    def _get_data_for_tickers(self):
        """Main method of this class
        1) gets data via REST
        2) parses data into Stock object
        3) adds stock object to list"""

        for t in self.tickers:
            stock_data = get_data_via_http(t, self.api_key)
            try:
                stock = parse_json_to_stock(stock_data)
                self.stocks.append(stock)
            except NoDataException:
                print 'No data for {0}'.format(t.upper())
