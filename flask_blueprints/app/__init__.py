# flask application factory
from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    with app.app_context():
        db.create_all()
    #launch the app
    return app