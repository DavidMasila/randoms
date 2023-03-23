from flask_login import LoginManager, current_user
from flask import Flask
from config import Config
from extensions import db, migrate, admin, principal, admin_role
from .controller import Controller
from flask_principal import identity_loaded, UserNeed


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
        admin.name = 'Control Panel'
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

        db.create_all()

        @identity_loaded.connect_via(app)
        def on_identity_loaded(sender, identity):
            # set the identity user object
            identity.user = current_user
            # add the user's id to the identity's UserNeed
            if hasattr(current_user, 'id'):
                identity.provides.add(UserNeed(current_user.id))

            # add the admin role is the user is an admin
            if hasattr(current_user, 'is_admin'):
                if current_user.is_admin:
                    identity.provides.add(admin_role)

        return app
