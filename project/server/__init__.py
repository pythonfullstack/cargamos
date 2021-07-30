from flask import Flask
from flask_migrate import Migrate

from project.server import config
from project.server import controllers
from project.server import database


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config.app_config[environment])
    controllers.init_app(app)
    database.init_app(app)
    migrate = Migrate(app, database.db)

    from project.server import models
    return app
