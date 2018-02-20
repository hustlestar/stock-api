from api.entity.transaction_processed import TransactionProcessed
from api.etl.extract.data_source import read_transaction_log
from api.etl.transform.parsers import parse_line_to_transaction
from api.etl.load.to_mysql import save_transaction_history


class TransactionList(object):
    def __init__(self, file_path, props):
        self.transactions = []
        self.props = props
        self.etl_load_skip = props.get('etl.load.skip') == 'true'
        self.file_path = file_path
        self._get_transaction_data()

    def _get_transaction_data(self):

        """Main method of this class
        1) gets data via REST
        2) parses data into Transaction Raw object
        3) processes transaction ti TransactionProcessed
        4) adds transaction object to list"""

        transaction_list = read_transaction_log(self.file_path)
        for t in transaction_list:
            raw_transaction = parse_line_to_transaction(t)
            if not self.etl_load_skip:
                save_transaction_history(raw_transaction, self.props)
            processed_transaction = TransactionProcessed(raw_transaction)
            print processed_transaction
            self.transactions.append(processed_transaction)
