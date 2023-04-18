from app import app, r, q
from flask import render_template, request
from app.tasks import count_words
from time import strftime


@app.route("/")
def index():
    return "Hellow world"


@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    jobs = q.jobs
    message = None

    if request.args:
        url = request.args.get("url")
        task = q.enqueue(count_words, url)

        jobs = q.jobs

        q_len = len(q)

        message = f"Task queued at {task.enqueued_at.strftime('%a %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

    return render_template("add_task.html", message = message,jobs = jobs)