from db_storage import db

def save_to_stock_history(stock_raw, props):
    con  = db.Connection(props)
    data_ = stock_raw.daily_data[0]
    con.insert(props.get('db.database') + '.' +'stock_history',
               stock_raw.symbol,
               data_.date,
               data_.open_,
               data_.high_,
               data_.low_,
               data_.close_,
               data_.volume_)
