from flask_login import LoginManager
from flask import Flask, redirect, url_for
from config import Config
from extensions import db, migrate, admin, principal, admin_role, admin_permission, user_permission
from .controller import Controller
from flask_principal import identity_changed, RoleNeed, Permission, identity_loaded, PermissionDenied
from flask_login import current_user

def create_app(config_class=Config):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(config_class)
        db.init_app(app)
        migrate.init_app(app, db)
        # call the Model tabel first for cascading use

        from .models import Seller

        # initialize admin
        admin.init_app(app)
        admin.name = 'Scorprog Admin'
        admin.template_mode = 'bootstrap5.2'
        admin.add_view(Controller(Seller, db.session))

        # use login manager to create session
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'auth.login'

        # create a user.loader
        @login_manager.user_loader
        def load_user(user_id):
            return Seller.query.get(int(user_id))

        # initialize permission management
        principal.init_app(app)

        # let's register blueprints requiring auth
        from .auth import auth as auth_bp
        app.register_blueprint(auth_bp)

        # blueprint not requiring auth
        from .main import main as main_bp
        app.register_blueprint(main_bp)


        #User Information Providers. 
        @identity_loaded.connect_via(app)
        def on_identity_loaded(sender, identity):
            if current_user.is_authenticated and current_user.is_admin:
                admin_permission = Permission(RoleNeed('admin'))
                identity.provides.add(RoleNeed('admin'))
                identity.provides.add(admin_permission)

        @app.errorhandler(PermissionDenied)
        def handle_permission_denied(e):
            return redirect(url_for('auth.login'))
        
        db.create_all()

        return app
