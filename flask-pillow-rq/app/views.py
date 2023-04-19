from app import app, r, q
from flask import render_template, request, flash
from app.tasks import count_words, create_imge_set
from time import strftime
import os
import secrets

app.config["SECRET_KEY"] = secrets.token_hex(16)
app.config["UPLOAD_DIRECTORY"] = "/home/masila/random/flask-pillow-rq/app/static/img/uploads"

@app.route("/")
def index():
    return "Hellow world"


# @app.route("/add-task", methods=["GET", "POST"])
# def add_task():

#     jobs = q.jobs
#     message = None

#     if request.args:
#         url = request.args.get("url")
#         task = q.enqueue(count_words, url)

#         jobs = q.jobs

#         q_len = len(q)

#         message = f"Task queued at {task.enqueued_at.strftime('%a %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

#     return render_template("add_task.html", message = message,jobs = jobs)

##### resising images ######

@app.route("/upload-image", methods=["GET","POST"])
def upload_image():

    message  = None
    if request.method == "POST" and request.files.get("image"):
        image = request.files.get("image")
        image_dir_name = secrets.token_hex(8)

        os.mkdir(os.path.join(app.config["UPLOAD_DIRECTORY"],  image_dir_name))

        image.save(os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name, image.filename))

        image_dir = os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name)

        q.enqueue(create_imge_set, image_dir, image.filename)

        flash("Image uploaded and sent for resizing","success")

        message = f"/image/{image_dir_name}/{image.filename.split('.')[0]}/{image.filename.split('.')[1]}"

    return render_template("upload_image.html", message = message)

@app.route("/image/<dir>/<img>/<ext>")
def view_image(dir, img, ext):
    return render_template("view_image.html", dir=dir, img=img, ext=ext)