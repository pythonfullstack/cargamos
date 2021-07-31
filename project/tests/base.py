from flask_testing import TestCase

from project.server import create_app
from project.server.database import db


class BaseTestCase(TestCase):
    """Base tests"""

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.reflect()
        db.drop_all()
