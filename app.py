import os
import unittest

from project.server import create_app
from project.server import database

app = create_app(os.getenv('FLASK_CONFIGURATION'))


def test():
    """
    Runs the unit tests without test coverage.
    :return:
    """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return True
    return False


def create_db():
    """Creates the db tables."""
    database.db.create_all()


if __name__ == "__main__":
    app.run()
