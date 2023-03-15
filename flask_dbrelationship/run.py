from app import app
from app.models import db, migrate, Comments, Post


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        migrate.init_app(app, db)
        app.run(debug=True)
