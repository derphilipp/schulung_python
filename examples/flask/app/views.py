# views.py

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
            { 'author': {'nickname': 'Peter'},
                'body': 'Mein Rezept fuer gebrannte Mandeln'
                },
            { 'author': {'nickname': 'Andrea'},
                'body': 'Die 10 besten Zombiefilme'
                }
            ]
    return render_template("index.html", title='Mein super Blog', posts=posts)
