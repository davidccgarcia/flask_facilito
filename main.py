#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_wtf import CsrfProtect

import forms

app = Flask(__name__)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    title = 'Curso de Flask'
    return render_template('login.html', title = title, form = login_form)

@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    response.set_cookie('customize_cookie', 'flask_facilito')
    return response

@app.route('/', methods = ['GET', 'POST'])
def index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print comment_form.username.data
        print comment_form.email.data
        print comment_form.comment.data
    else:
        print 'Error en el formulario'

    customize_cookie = request.cookies.get('customize_cookie', 'Undefined')
    print customize_cookie
    title = 'Curso de Fask'
    return render_template('index.html', title = title, form = comment_form)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
