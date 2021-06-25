from flask import Flask, render_template
from database import (
    SELECT_WHERE,
    SELECT
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories/<category>')
def category(category):
    q = None
    if category == "all":
        q = SELECT(
            'products', [
                'id',
                'name',
                'category',
                'image_src',
                'description',
            ]
        )
    else:
        q = SELECT_WHERE(
            'products', [
                'id',
                'name',
                'category',
                'image_src',
                'description',
            ],
            'category',
            category
        )
    return render_template('index.html', category=q)
