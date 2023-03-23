from app import create_app
from flask import Blueprint, render_template, url_for, redirect, request, flash
from .models import Seller
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, logout_user, login_required
from .forms import Loginform, Signupform
from extensions import db, admin_permission, admin_role, user_role
from flask_principal import Identity, identity_changed, AnonymousIdentity, RoleNeed, identity_loaded, UserNeed
import app

auth = Blueprint('auth', __name__)


@auth.route("/login",methods = ['GET', 'POST'])
def login():
    form = Loginform()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if form.validate_on_submit():
        if request.method == 'POST':
            email = form.email.data
            password = form.password.data
            remember = True if request.form.get('remember') else False

            user = Seller.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                flash("Please check your log in credentials")
                return redirect(url_for('auth.login'))
            else:
                identity = Identity(user.id)
                #give the user the role of the admin
                identity_changed.send(app, identity = identity)
                #nofify the app that identity has changed
                login_user(user=user, remember=remember)
                return redirect(url_for('main.index'))
            
    return render_template("/login.html", form = form)

@auth.route("/signup", methods=['POST','GET'])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        is_admin = False
        
        user = Seller.query.filter_by(email=email).first()
        if not user:
            new_user = Seller(email = email, username = username,
                              password=generate_password_hash(password, method='sha256'),
                              is_admin = is_admin)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash("That email elready exists")
            return redirect(url_for('auth.signup'))
    return render_template("signup.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    #tell flask principal the user is anonymous
    identity_changed.send(app, identity = AnonymousIdentity())
    return redirect(url_for('main.index'))


@auth.route("/check")
@admin_permission.require()
def check():
    return "only if you are admin"