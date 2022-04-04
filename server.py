from flask import Flask
import random


app = Flask(__name__)


@app.route('/')
def index():
    return '''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                <li><a href="/read/1/">html</a></li>
                <li><a href="/read/2/">css</a></li>
                <li><a href="/read/3/">javascript</a></li>
            </ol>
        </body>
    </html>
    '''

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read ' + id

app.run(port=5000, debug=True)
    