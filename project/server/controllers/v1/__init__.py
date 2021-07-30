from flask import Blueprint
from flask_restx import Api

from project.server.controllers.v1.store import api as store
from project.server.controllers.v1.production import api as production
from project.server.controllers.v1.inventory import api as inventory

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint, title='Test REST API', version='1.0', description='This is Test REST API from Cargamos')

api.add_namespace(store)
api.add_namespace(production)
api.add_namespace(inventory)
