from flask import Flask
from rq import Queue
import redis

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)

from app import views
from app import tasks