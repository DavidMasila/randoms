import secrets

class Config:
    SECRET_KEY= secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/permissions_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False