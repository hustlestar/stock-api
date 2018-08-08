from datetime import datetime

from api import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    type = db.Column(db.String(10), nullable=True)
    registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sex = db.Column(db.String(60), nullable=True)
    image_file = db.Column(db.String(60), nullable=False, default='pics/default.jpg')
    #watchlist = db.relationship('Post', backref='watcher', lazy=True)

    def __repr__(self):
        return "User('{self.username}', '{self.email}', '{self.image_file}')".format(self=self)

class WatchList(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    ticker_id = db.Column(db.Integer, db.ForeignKey('ticker.id'), nullable=False, primary_key=True)

    def __repr__(self):
        return "WatchList('{self.user_id}', '{self.ticker_id}')".format(self=self)

class Ticker(db.Model):
    ticker = db.Column(db.String(10), nullable=False, primary_key=True)
    price_date = db.Column(db.DateTime, nullable=False, primary_key=True)
    open = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    vol = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "{self.ticker}('{self.price_date}', '{self.close}', '{self.vol}')".format(self=self)