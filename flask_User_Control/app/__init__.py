from flask import Flask
from flask_login import LoginManager, current_user
from flask_principal import Principal, identity_loaded, current_app, RoleNeed, Permission
from .models import Seller
from .extensions import db
login_manager = LoginManager()
principal = Principal()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/permissions_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # Initialize Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    @login_manager.user_loader
    def load_user(user_id):
        return Seller.query.get(int(user_id))
    
    # Initialize Flask-Principal
    principal.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # get the user's roles from the database or some other source
        if current_user.is_authenticated and current_user.is_admin:
            admin_role = Permission(RoleNeed('admin'))
            identity.provides.add(RoleNeed('admin'))
            identity.provides.add(admin_role)

    # Register blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
