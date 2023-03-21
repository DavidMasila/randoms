from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5432/authenticate'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'flask_development i know relax'
    db.init_app(app)

    with app.app_context():
        # blueprint for auth routes in our app
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # blueprint for non-auth parts of app
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        #importing the models to make sure they are resgistered with SQLAlchemy
        from app.models import User
        db.create_all()
        return app