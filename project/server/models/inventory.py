from project.server.database import db
from project.server.models.production import Production
from project.server.models.store import Store
from sqlalchemy.sql import func


class Inventory(db.Model):
    __tablename__ = 'inventories'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=False)
    stock = db.Column(db.Integer, default=0)

    def json(self):
        return {
            'id': self.id,
            'store_id': self.store_id,
            'production_id': self.production_id,
            'stock': self.stock
        }

    @staticmethod
    def update_stocks(_id, stocks):
        inventory = Inventory.query.get(_id)
        inventory.stock += stocks
        db.session.add(inventory)
        db.session.commit()
        return inventory.json()

    @staticmethod
    def get_all():
        return [inventory.json() for inventory in Inventory.query.all()]

    @staticmethod
    def get_inventory(_id):
        return Inventory.query.filter_by(id=_id).first()

    @staticmethod
    def create(data):
        store_id = data['store_id']
        if Store.query.get(store_id) is None:
            return False, f"Store {store_id} doesn't exist"
        production_id = data['production_id']
        if Production.query.get(production_id) is None:
            return False, f"Production {production_id} doesn't exist"
        stock = data['stock']
        if stock < 0:
            return False, "Stock must be at least 0"
        inventory = Inventory(store_id=store_id, production_id=production_id, stock=stock)
        db.session.add(inventory)
        db.session.commit()
        return True, inventory.json()

    @staticmethod
    def delete(_id):
        inventory = Inventory.query.get(_id)
        if inventory is None:
            return False
        else:
            db.session.delete(inventory)
            db.session.commit()
            return True

    @staticmethod
    def get_all_stocks(production_id):
        stocks = db.session.query(func.sum(Inventory.stock).label('stocks'), Inventory).filter_by(
            production_id=production_id)
        if stocks.first().stocks is None:
            return False, f"Production {production_id} doesn't exist"
        return True, {
            'stocks': stocks.first().stocks,
        }
