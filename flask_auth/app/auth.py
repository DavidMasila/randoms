# require authentication for persion to view the pages here
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from . import db
auth = Blueprint('auth', __name__)



@auth.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')





@auth.route('/login_post', methods=['POST'])
def login_post():
    # login code goes here
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) 
    #after the verification log in the user
    login_user(user, remember = remember)
    return redirect(url_for('main.profile'))





@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email Address has an acc already")
            return redirect(url_for('auth.signup'))
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template("/signup.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))