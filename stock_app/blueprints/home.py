from flask import Blueprint, render_template, url_for, redirect, request

home = Blueprint('home', __name__)

@home.route("/")
def home_page():
    return render_template("home/index.html")

@home.route("/search", methods=['POST'])
def search():
    return  redirect(url_for('stock.quote', ticker=request.form['ticker']))
