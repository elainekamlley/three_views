# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/second_view')
def second_view():
	return render_template('second_view.html')

@app.route('/third_view')
def third_view():
	return render_template('third_view.html')