from flask import Flask
import secrets

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = secrets.token_hex(16)


from app import views
from app import models
