import os
import unittest

from project.server import create_app
from project.server.tasks import celery_app as celery
from updated_packages.flask_script import Manager

app = create_app(os.getenv('FLASK_CONFIGURATION'))

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


if __name__ == "__main__":
    manager.run()
