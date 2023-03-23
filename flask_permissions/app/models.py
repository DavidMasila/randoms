from extensions import db
from flask_login import UserMixin

class Seller(UserMixin, db.Model):
    __tablename__ = 'seller'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable=False)
    username =  db.Column(db.String(50), nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)
    is_admin = db.Column(db.Boolean, nullable = False, default = False)