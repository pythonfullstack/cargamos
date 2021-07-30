from project.server.database import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    inventories = db.relationship('Inventory', backref='store', lazy='dynamic')

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    @staticmethod
    def create(data):
        name = data['name']
        address = data['address']
        store = Store(name=name, address=address)
        db.session.add(store)
        db.session.commit()
        return store.json()

    @staticmethod
    def get_all():
        return [Store.json(store) for store in Store.query.all()]

    @staticmethod
    def get_store(_id):
        return Store.query.filter_by(id=_id).first()

    @staticmethod
    def delete(_id):
        store = Store.query.get(_id)
        if store is None:
            return False
        else:
            db.session.delete(store)
            db.session.commit()
            return True

    @staticmethod
    def update(_id, data):
        store = Store.query.get(_id)
        if 'name' in data:
            store.name = data['name']
        if 'address' in data:
            store.data = data['address']
        db.session.add(store)
        db.session.commit()
        return store