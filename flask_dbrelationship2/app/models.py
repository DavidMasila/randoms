from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/rela_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# creating the association table for the many to many relationship
post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.Text, nullable=False)
    comments = db.relationship("Comments", backref='post', lazy=True)
    tags = db.relationship('Tags', secondary=post_tag, backref='posts')

    def __repr__(self):
        return f"<Post ${self.title}>"


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f"<Comment ${self.content[:20]}>"


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(50))

    def __repr__(self):
        return f"<Tag name {self.tag_name}"

with app.app_context():
    db.create_all()
    migrate.init_app(app, db)
    db.session.commit()