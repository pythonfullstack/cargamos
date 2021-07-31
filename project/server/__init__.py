from flask import Flask
from flask_migrate import Migrate

from project.server import config
from project.server import controllers
from project.server.database import db

migrate = Migrate()


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config.app_config[environment])
    database.init_app(app)
    controllers.init_app(app)
    migrate.init_app(app, db)

    from project.server import models

    return app
