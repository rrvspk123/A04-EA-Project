from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm, WebForm
from app.models import User, Post, Website

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html.j2')

@app.route('/wbase')
def wbase():
    website = Website.query.all()
    return render_template("wbase.html.j2",website=website)

@app.route('/addweb', methods=['GET', 'POST'])
def addweb():
    form = WebForm()
    if form.validate_on_submit():
        webdata = Website(link_v=form.link_v.data, link_p=form.link_p.data, title=form.title.data, middle_data=form.middle_data.data)
        db.session.add(webdata)
        db.session.commit()
        return redirect(url_for('addweb'))
    return render_template('addweb.html.j2', form=form)

if __name__ == '__main__':
    app.run(debug=True)
 







