import os
import unittest
from flask_script import Manager
from project.server import create_app
from project.server import database

manager = Manager(create_app(os.getenv('FLASK_CONFIGURATION')))


@manager.command
def test():
    """
    Runs the unit tests without test coverage.
    :return:
    """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    # result = unittest.TextTestRunner(verbosity=2).run(tests)
    # if result.wasSuccessful():
    #     return True
    # return False


@manager.command
def create_db():
    """Creates the db tables."""
    database.db.create_all()


if __name__ == "__main__":
    manager.run()
