from flask_restx import Namespace, Resource, fields
from project.server.models import Inventory

api = Namespace('inventories', 'Inventory Operations')

inventory_stock = api.model('Inventory Stock', {
    'stock': fields.Integer(required=True, description='The inventory the number of stocks'),
})

inventory = api.inherit('Inventory', inventory_stock, {
    'id': fields.Integer(readonly=True, description='The inventory unique identifier'),
    'store_id': fields.Integer(required=True, description='The inventory store identifier'),
    'production_id': fields.Integer(required=True, description='The inventory production identifier'),
})


@api.route("/")
class InventoryList(Resource):
    """Shows a list of all inventories, and lets you POST to add new inventories"""

    @api.doc('list_inventories')
    @api.marshal_list_with(inventory)
    def get(self):
        """List of all inventories"""
        return Inventory.get_all()

    @api.doc('create_inventory')
    @api.expect(inventory)
    @api.marshal_with(inventory)
    def post(self):
        """Create a new inventory"""
        success, data = Inventory.create(api.payload)
        if success:
            return data, 201
        else:
            return api.abort(404, data)


@api.route("/<int:inventory_id>")
@api.response(404, 'Inventory not found')
@api.param('inventory_id', 'The inventory identifier')
class InventoryResource(Resource):
    """Show a single inventory item and lets you delete them"""

    @api.doc('get_inventory')
    @api.marshal_with(inventory)
    def get(self, inventory_id):
        """fetch a given inventory"""
        result = Inventory.get_inventory(inventory_id)
        if result is not None:
            return result
        else:
            return api.abort(404, f"Inventory {inventory_id} doesn't exist")

    @api.doc('delete_inventory')
    @api.response(204, 'inventory deleted')
    def delete(self, inventory_id):
        result = Inventory.delete(inventory_id)
        if result:
            return '', 204
        else:
            return api.abort(404, f"Inventory {inventory_id} doesn't exist")

    @api.expect(inventory_stock)
    def put(self, inventory_id):
        """change inventory stock"""
        stocks = api.payload['stock']
        return Inventory.update_stocks(inventory_id, stocks)


@api.route("/get-all-stocks/<int:production_id>")
@api.response(404, 'Production not found')
@api.doc('get all stocks')
class AllStocks(Resource):
    """get all stocks for a given production"""

    @api.doc('get_all_stocks')
    def get(self, production_id):
        """get all stocks for a given production"""
        success, data = Inventory.get_all_stocks(production_id)
        if success:
            return data
        else:
            return api.abort(404, data)
