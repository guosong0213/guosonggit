#!/usr/bin/env python

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    app.debug = True
    app.run()

