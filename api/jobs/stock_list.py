from api.entity.stock_processed import StockProcessed
from api.etl.extract.data_source import get_data_alpha_vantage
from api.etl.transform.no_data_exception import NoDataException
from api.etl.transform.parsers import parse_alpha_vantage_json_to_stock
from api.etl.load.to_mysql import save_stock_history


class StockList:
    def __init__(self, tickers, props):
        self.tickers = tickers
        self.stocks = []
        self.api_key = props.get('api.key')
        self.props = props
        self._get_data_for_tickers()

    def _get_data_for_tickers(self):
        """Main method of this class
        1) gets data via REST
        2) parses data into Stock object
        3) adds stock object to list"""

        for t in self.tickers:
            stock_data = get_data_alpha_vantage(t, self.props)
            try:
                stock_raw = parse_alpha_vantage_json_to_stock(stock_data)
                save_stock_history(stock_raw, self.props)
                stock_processed = StockProcessed(stock_raw)
                self.stocks.append(stock_processed)
            except NoDataException:
                print 'No data for {0}'.format(t.upper())
