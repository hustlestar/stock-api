import mysql.connector as connector

class Connection(object):
    def __init__(self):
        pass

def get_connection(props):
    return connector.connect(user=props.get('db.user'),
                            password=props.get('db.password'),
                            host=props.get('db.host'),
                            port=props.get('db.port'),
                            database=props.get('db.database')).cursor()

def insert(cursor, stmt, **args):
    cursor.execute(
        """INSERT INTO stockdb.stock_history
        (SH_TICKER,
        SH_DATE,
        SH_OPEN,
        SH_HI,
        SH_LO,
        SH_CLOSE,
        SH_VOL)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s);""",
        (stock.symbol, last_day.date, last_day.open_, last_day.high_, last_day.low_, last_day.close_, last_day.volume_))
    pass

if __name__ == '__main__':
    import api.main

    stock = api.main.parse_stock_json(api.main.get_data('AAPL', 'RWOH7RVGZIFSZK4X'))
    last_day = stock.daily_data[-1]




    cnx.commit()
    cursor.close()
    cnx.close()
