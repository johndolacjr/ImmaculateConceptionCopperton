#Anything the user can navigate too, goes here. The only exception is anything relating to authentication--> that will go in auth.py file

from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/login')
def home():
    return "<h1>Test</h1>"

