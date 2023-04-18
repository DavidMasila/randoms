from flask import Flask, request
import redis
from rq import Queue
import time
import bs4

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


def background_task(n):
    delay = 2
    print(f"Task running,simmulating a {delay} second delay")
    time.sleep(delay)

    print(len(n))
    print("Task Complete")

    return len(n)


@app.route("/task")
def add_task():
    if request.args.get("n"):
        job = q.enqueue(background_task, request.args.get("n"))
        q_len = len(q)

        return f"Task ({job.id}) added to queue at ({job.enqueued_at}). {q_len} tasks in queue"

    return "No value for n provided"

if __name__ == "__main__":
    app.run(debug=True)