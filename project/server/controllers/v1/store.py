from flask_restx import Namespace, Resource, fields
from project.server.models import Store

api = Namespace('stores', 'Store Operations')

store = api.model('Store', {
    'id': fields.Integer(readonly=True, description='The store unique identifier'),
    'name': fields.String(required=True, description='The store name'),
    'address': fields.String(required=True, description='The store address'),
})


@api.route("/")
class StoreList(Resource):
    """Shows a list of all stores, and lets you POST to add new stores"""

    @api.doc('list_stores')
    @api.marshal_list_with(store)
    def get(self):
        """List of all stores"""
        return Store.get_all()

    @api.doc('create_store')
    @api.expect(store)
    @api.marshal_with(store)
    def post(self):
        """Create a new Store"""
        result = Store.create(api.payload)
        return result, 201


@api.route("/<int:store_id>")
@api.response(404, 'Store not found')
@api.param('store_id', 'The store identifier')
class StoreResource(Resource):
    """Show a single store item and lets you delete them"""

    @api.doc('get_store')
    @api.marshal_with(store)
    def get(self, store_id):
        """fetch a given store"""
        result = Store.get_store(store_id)
        if result is not None:
            return result
        else:
            return api.abort(404, f"Store {store_id} doesn't exist")

    @api.doc('delete store')
    @api.response(204, 'Store deleted')
    def delete(self, store_id):
        result = Store.delete(store_id)
        if result:
            return '', 204
        else:
            return api.abort(404, f"Store {store_id} doesn't exist")

    @api.expect(store)
    @api.marshal_with(store)
    def put(self, store_id):
        """patch or put store data"""
        return Store.update(store_id, api.payload)
