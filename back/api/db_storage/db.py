import mysql.connector as connector
import etl.extract.data_source


class Connection(object):
    def __init__(self, props):
        self.connection = self._get_connection(props)
        self.cursor = self._get_cursor()

    def _get_connection(self, props):
        return connector.connect(user=props.get('db.user'),
                                 password=props.get('db.password'),
                                 host=props.get('db.host'),
                                 port=int(props.get('db.port')),
                                 database=props.get('db.database'))

    def _get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def insert(self, table_name, *args):
        stmt = 'INSERT INTO {0} VALUES ('.format(table_name)
        for val in args:
            if isinstance(val, unicode):
                stmt = stmt + "'" + str(val) + "', "
            else:
                stmt = stmt + str(val) + ", "
        stmt = stmt[:-2] + ');'
        #print stmt
        self.cursor.execute(stmt)
        self.commit()


if __name__ == '__main__':
    import api.main

    stock = api.main.parse_stock_json(api.etl.extract.data_source.get_data_alpha_vantage('AAPL', 'RWOH7RVGZIFSZK4X'))
    last_day = stock.daily_data[0]
