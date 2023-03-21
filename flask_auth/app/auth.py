# require authentication for persion to view the pages here
from flask import Blueprint, render_template, redirect, url_for, request, flash
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
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 
    
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
