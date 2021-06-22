from flask import Flask, render_template
from database import (
    SELECT_WHERE
)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories/<category>')
def category(category):
    q = SELECT_WHERE(
        'products', [
            'id',
            'name',
            'category',
            'description',
        ],
        'category',
        category
    )
    return render_template('index.html', category=q)
