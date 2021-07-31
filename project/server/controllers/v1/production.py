from flask_restx import Namespace, Resource, fields

from project.server.models import Production
from project.server.tasks import task_with_celery, threads

api = Namespace('productions', 'Production Operations')

production = api.model('Production', {
    'id': fields.Integer(readonly=True, description='The production unique identifier'),
    'sku': fields.String(required=True, description='The production sku'),
})


@api.route("/")
class ProductionList(Resource):
    """Shows a list of all productions, and lets you POST to add new productions"""

    @api.doc('list_production')
    @api.marshal_list_with(production)
    def get(self):
        """List of all productions"""
        return Production.get_all()

    @api.doc('create_production')
    @api.expect(production)
    @api.marshal_with(production)
    def post(self):
        """Create a new production"""
        result = Production.create(api.payload)
        # Asynchronous long task that we don't have to know the output
        task_with_celery.delay()
        threads.async_task_with_threading()

        return result, 201


@api.route("/<int:production_id>")
@api.response(404, 'Production not found')
@api.param('production_id', 'The production identifier')
class ProductionResource(Resource):
    """Show a single production item and lets you delete them"""

    @api.doc('get_production')
    @api.marshal_with(production)
    def get(self, production_id):
        """fetch a given production"""
        result = Production.get_product(production_id)
        if result is not None:
            return result
        else:
            return api.abort(404, f"Production {production_id} doesn't exist")

    @api.doc('delete production')
    @api.response(204, 'production deleted')
    def delete(self, production_id):
        result = Production.delete(production_id)
        if result:
            return '', 204
        else:
            return api.abort(404, f"Production {production_id} doesn't exist")

    @api.expect(production)
    @api.marshal_with(production)
    def put(self, production_id):
        """patch or put production data"""
        return Production.update(production_id, api.payload)
