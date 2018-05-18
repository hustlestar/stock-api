import os
from flask import Flask, render_template, Markup, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import forms
import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = "fuckall"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{self.username}', '{self.email}', '{self.image_file}')".format(self=self)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/plot')
def get_ticker():
    secrets_path = '../secrets/credentials.properties'
    secrets_path = os.path.normpath(secrets_path)
    props = utils.read_properties(secrets_path)

    stock_raw = utils.get_stock_raw('AAPL', props)
    chart_div = utils.get_chart_for(stock_raw, props)

    return render_template("ticker.html", chart=Markup(chart_div))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!'.format(form=form), 'success')
        return redirect(url_for('home'))
    return render_template("sign_up.html", title='Sign Up Now', form=form)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = forms.SignInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("sign_in.html", title='Sign In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
