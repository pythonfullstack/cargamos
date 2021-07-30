from project.server.controllers.v1 import blueprint as api_v1


def init_app(app):
    app.register_blueprint(api_v1)
