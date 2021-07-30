# project/server/tests/test_config.py


import unittest
from abc import ABC

from flask import current_app
from flask_testing import TestCase

from project.server import create_app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        return create_app('development')

    def test_app_is_development(self):
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        return create_app('testing')

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['DEBUG'])


class TestProductionConfig(TestCase):
    def create_app(self):
        return create_app('production')

    def test_app_is_production(self):
        self.assertTrue(self.app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
