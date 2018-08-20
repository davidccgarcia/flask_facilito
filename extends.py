#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'David'
    return render_template('index.html', name = name)

@app.route('/client')
def client():
    list_name = ['David', 'Natalia', 'Sara', 'Jhon']
    return render_template('client.html', names = list_name)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
