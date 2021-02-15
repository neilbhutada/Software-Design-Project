from flask import Blueprint, render_template, url_for, request, redirect, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

@auth.route('/login/user', methods = ['POST', 'GET'])
def loginuser():
    name = request.form.get('user')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(password=password).first()
    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))