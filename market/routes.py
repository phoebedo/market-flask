# from flask import Flask, render_template
# app = Flask(__name__)
from market import app
from flask import render_template
from market.models import Item
@app.route("/")
@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
# dynamic route
@app.route("/about/<username>")
def profile(username):
    return f"this is the page of {username}"