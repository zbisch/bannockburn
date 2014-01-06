from app import app
from flask import render_template

import libs

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World! wirrrrr"


@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/<user>/view_pomos')
def view_pomos(user):
    pomos = libs.get_pomos(user=user)
    return str(pomos)
