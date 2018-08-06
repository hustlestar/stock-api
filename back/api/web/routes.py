import os

import flask_login
from api import app, db, bcrypt, utils, props
from api import forms
from api import utils
from api.user_db import models
from flask import render_template, flash, url_for, request
from markupsafe import Markup
from werkzeug.utils import redirect

@app.route('/')
@app.route('/home')
def home():
    print "Nihuia"
    return render_template("home.html")


# @login_required
@app.route('/plot')
def get_ticker():
    stock_raw = utils.get_stock_raw('AAPL', props)
    chart_div = utils.get_chart_for(stock_raw, props)

    return render_template("ticker.html", chart=Markup(chart_div))


@app.route('/register', methods=['GET', 'POST'])
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    print db.metadata.tables.keys()
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('home'))
    form = forms.SignUpForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = models.User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('sign_in'))

    return render_template('sign_up.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    print db.metadata.tables.keys()
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('home'))
    form = forms.SignInForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        #print(models.User.query.all())
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flask_login.login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("sign_in.html", title='Sign In', form=form)


@app.route("/logout")
@app.route("/sign_out")
@flask_login.login_required
def sign_out():
    flask_login.logout_user()
    return redirect(url_for('home'))
