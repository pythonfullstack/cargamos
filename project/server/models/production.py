from project.server.database import db


class Production(db.Model):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    sku = db.Column(db.String(20), unique=True)
    inventories = db.relationship('Inventory', backref='production', lazy='dynamic')

    def json(self):
        return {
            'id': self.id,
            'sku': self.sku
        }

    @staticmethod
    def create(data):
        sku = data['sku']
        production = Production(sku=sku)
        db.session.add(production)
        db.session.commit()
        return production.json()

    @staticmethod
    def get_all():
        return [Production.json(production) for production in Production.query.all()]

    @staticmethod
    def get_product(_id):
        return Production.query.filter_by(id=_id).first()

    @staticmethod
    def delete(_id):
        production = Production.query.get(_id)
        if production is None:
            return False
        else:
            db.session.delete(production)
            db.session.commit()
            return True

    @staticmethod
    def update(_id, data):
        production = Production.query.get(_id)
        if 'sku' in data:
            production.sku = data['sku']
        db.session.add(production)
        db.session.commit()
        return production