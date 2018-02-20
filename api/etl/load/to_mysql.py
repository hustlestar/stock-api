from db_storage import db


def save_to_stock_history(stock_raw, props):
    con = db.Connection(props)
    data_ = stock_raw.daily_data[0]
    con.insert(props.get('db.database') + '.' + 'stock_history',
               stock_raw.ticker,
               data_.date,
               data_.open_,
               data_.high_,
               data_.low_,
               data_.close_,
               data_.volume_)


def save_transaction_history(transaction_raw, props):
    con = db.Connection(props)
    con.insert(props.get('db.database') + '.' + 'transaction',
               transaction_raw.date,
               transaction_raw.ticker,
               transaction_raw.direction,
               transaction_raw.price)

