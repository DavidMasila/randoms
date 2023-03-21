import os
import secrets


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'postgresql://postgres:postgres@localhost:5432/auth'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
