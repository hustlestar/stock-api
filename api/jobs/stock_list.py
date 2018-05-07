from entity.stock_processed import StockProcessed
from etl.extract.data_source import get_data_alpha_vantage, AlphaVantageAPI
from etl.transform.no_data_exception import NoDataException
from etl.transform.parsers import parse_alpha_vantage_json_to_stock
from etl.load.to_mysql import save_to_stock_history


class StockList:
    def __init__(self, tickers, props):
        self.tickers = tickers
        self.stocks_processed = []
        self.etl_load_skip = props.get('etl.load.skip') == 'true'
        self.api_key = props.get('api.key')
        self.props = props
        self._get_data_for_tickers()

    def _get_data_for_tickers(self):
        """Main method of this class
        1) gets data via REST
        2) parses data into Stock object
        3) adds stock object to list"""
        api = AlphaVantageAPI(self.props)
        for ticker in self.tickers:
            stock_data = api.get_data_for_ticker(ticker)
            try:
                stock_raw = parse_alpha_vantage_json_to_stock(stock_data)
                if not self.etl_load_skip:
                    save_to_stock_history(stock_raw, self.props)
                stock_processed = StockProcessed(stock_raw)
                self.stocks_processed.append(stock_processed)
            except NoDataException:
                print 'No data for {0}'.format(ticker.upper())
