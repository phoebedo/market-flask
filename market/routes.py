# from flask import Flask, render_template
# app = Flask(__name__)
from crypt import methods
from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db
@app.route("/")
@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f'ERROR: {err[0]}', category='danger')
        
    return render_template("register.html", form=form)

# dynamic route
# @app.route("/about/<username>")
# def profile(username):
#     return f"this is the page of {username}"