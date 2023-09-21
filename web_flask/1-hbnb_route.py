#!/usr/bin/python3
'''A Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''home page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb page.'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
