from app import app
from flask import redirect, url_for, request, render_template
from app.models import Post, Comments, db, Tags

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("/index.html", posts = posts)


@app.route("/<int:post_id>", methods=['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment = Comments(comment=request.form['content'], post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    return render_template("post.html", post=post)

@app.route("/comments")
def comments():
    comments = Comments.query.order_by(Comments.id.desc()).all()
    return render_template("/comments.html", comments=comments)

@app.route("/comments/<int:comment_id>/delete", methods=['GET','POST'])
def delete_comment(comment_id):
    comment = Comments.query.get_or_404(comment_id)
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))

@app.route("/tag/<int:post_id>/add_tag", methods=['GET','POST'])
def add_tag(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        tag = request.form['tag']
        new_tag = Tags(tag_name=tag)
        post.tags.append(new_tag)
        db.session.add(post)
        db.session.add(new_tag)
        db.session.commit()
    return render_template("post.html", post=post)

@app.route("/topics")
def topics():
    tags = Tags.query.all()
    return render_template("/topics.html", tags=tags)