
from flask import render_template, flash, redirect, url_for, request, g
from app import app, db








@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html.j2")








