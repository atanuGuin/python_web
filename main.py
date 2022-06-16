#!/usr/bin/python
from flask import Flask, escape, request
from flask import Flask, url_for
from markupsafe import escape
from flask import render_template
import logging

# Create an instance of this class
app = Flask(__name__)

# Logging configuration
logging.basicConfig(filename='demo.log', level=logging.DEBUG)


# Use the route() decorator to bind a function to a URL.
@app.route('/')
def index():
    app.logger.info('Processing default request')
    # return 'Index Page'
    return render_template('index.html')


@app.route('/index.html')
def index_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
