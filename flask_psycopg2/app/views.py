from app import app
from flask import render_template, request, redirect, url_for, flash, make_response
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database = 'flask_db',
        user= "postgres",
        password = "postgres"
    )

    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    cur=conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("/index.html", books = books)


@app.route("/create/", methods =["POST","GET"])
def create():
    if request.method == "POST":
        title=request.form.get('title')
        author = request.form['author']
        pages_num = request.form['pages_num']
        pages_num = int(float(pages_num))
        review = request.form.get('review')

        conn = get_db_connection()
        cur  = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES(%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template("/create.html")

