from flask import Flask
import secrets

app = Flask(__name__)

key = secrets.token_hex(16)
app.config['SECRET_KEY'] = key


from app import models
from app import forms
from app import views
