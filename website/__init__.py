#NOTE FOR CHRIS: The double underscores makes the website folder a python package. 
from flask import Flask

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Secret Key is Sacred'

    return app
