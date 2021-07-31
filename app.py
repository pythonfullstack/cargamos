import unittest

from project.server import database
from project.server.tasks import *
from updated_packages.flask_script import Manager

manager = Manager(app)


@manager.command
def test():
    """
    Runs the unit tests without test coverage.
    :return:
    """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    database.db.create_all()


if __name__ == "__main__":
    manager.run()
