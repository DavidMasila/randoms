from flask import Flask

app=Flask(__name__)
app.config["SECRET_KEY"] = "masiladavid"

from app import views
from app import forms