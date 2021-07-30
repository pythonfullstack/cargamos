import unittest

from project.server.database import db
from project.server.models import Store
from project.tests.base import BaseTestCase
from project.tests.helper import response_decode


class TestStore(BaseTestCase):
    def test_create_store(self):
        store = Store(name="test store", address='test address')
        db.session.add(store)
        db.session.commit()
        store_id = store.id
        response = self.client.get(f'/api/v1/stores/{store_id}', content_type='application/json')
        data = response_decode(response)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['name'] == 'test store')
        self.assertTrue(data['address'] == 'test address')

    def test_all_stores(self):
        dummy = [
            {'name': 'test store 1', 'address': 'test address 1'},
            {'name': 'test store 2', 'address': 'test address 2'},
        ]
        for store in dummy:
            store = Store(name=store['name'], address=store['address'])
            db.session.add(store)
            db.session.commit()
        response = self.client.get(f'/api/v1/stores/', content_type='application/json')
        data = response_decode(response)
        self.assertTrue(len(data) == 2)
        self.assertTrue(data[0]['name'] == 'test store 1')
        self.assertTrue(data[1]['address'] == 'test address 2')

        store_id = data[0]['id']
        response = self.client.delete(f'/api/v1/stores/{store_id}', content_type='application/json')
        self.assertEqual(response.status_code, 204)

        response = self.client.get(f'/api/v1/stores/', content_type='application/json')
        data = response_decode(response)
        self.assertTrue(len(data) == 1)


if __name__ == '__main__':
    unittest.main()
