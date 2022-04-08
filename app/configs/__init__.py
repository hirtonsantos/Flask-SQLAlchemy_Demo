import imp
from flask import Flask
from app.configs import database


def create_app():
    # Instanciando o Flask
    app = Flask(__name__)

    database.init_app(app)

    return app
