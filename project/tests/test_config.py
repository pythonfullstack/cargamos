# project/server/tests/test_config.py


import unittest
from abc import ABC

from flask import current_app
from flask_testing import TestCase

from project.server import create_app


class TestDevelopmentConfig(TestCase, ABC):

    def test_app_is_development(self):
        app = create_app('development')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase, ABC):

    def test_app_is_testing(self):
        app = create_app('testing')
        self.assertTrue(app.config['DEBUG'])


class TestProductionConfig(TestCase, ABC):

    def test_app_is_production(self):
        app = create_app('production')
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
