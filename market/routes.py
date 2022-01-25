# from flask import Flask, render_template
# app = Flask(__name__)
from crypt import methods
from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import LoginForm, RegisterForm
from market import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as: {user_to_create.username}',category='success')

        return redirect(url_for("market_page"))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'ERROR: {err[0]}', category='danger')
        
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        current_user = User.query.filter_by(username=form.username.data).first()
        if current_user and current_user.check_password(current_password = form.password.data):
            login_user(current_user)
            flash(f'Success! You are logged in as: {current_user.username}',category='success')
            return redirect(url_for("market_page"))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)
@app.route('/logout')
def logout_page():
    logout_user()

    return render_template("home.html")



# dynamic route
# @app.route("/about/<username>")
# def profile(username):
#     return f"this is the page of {username}"