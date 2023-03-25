from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from flask_principal import Identity, identity_changed, Permission, RoleNeed
from .forms import Loginform, Signupform
from .models import Seller
from .extensions import db

auth_bp = Blueprint('auth', __name__, template_folder='templates')

admin_permission = Permission(RoleNeed('admin'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form=Loginform()
    if current_user.is_authenticated:
        return redirect(url_for('auth.admin_panel'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False

        user = Seller.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
                flash("Please check your log in credentials")
                return redirect(url_for('auth.login'))

        login_user(user, remember=remember)

        # Set the identity of the current user
        identity = Identity(user.id)
        identity_changed.send(current_app._get_current_object(), identity=identity)
    return render_template('login.html', form=form)

@auth_bp.route("/signup", methods=['POST', 'GET'])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        is_admin = False

        user = Seller.query.filter_by(email=email).first()
        if not user:
            new_user = Seller(email=email, username=username,
                              password=generate_password_hash(
                                  password, method='sha256'),
                              is_admin=is_admin)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash("That email elready exists")
            return redirect(url_for('auth.signup'))
    return render_template("signup.html", form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    # Remove the identity of the current user
    identity_changed.send(current_app._get_current_object(), identity=Identity(0))
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/admin')
@admin_permission.require(http_exception=403)
@login_required
def admin_panel():
    return 'Welcome, admin!'
