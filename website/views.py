from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect, session, url_for, flash
views = Blueprint('views', __name__)


# add sign in page, log in page, grocery page, add to list page, 





@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        something = request.form['something']
        session['something'] = something
        flash('已加入session', category='success')
        print(session['something'])
    return render_template("home.html")
