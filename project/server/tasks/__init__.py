from celery import Celery
from project.server import create_app
import os

app = create_app(os.getenv('FLASK_CONFIGURATION'))
celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@celery.task
def async_task():
    import time
    time.sleep(5)
    return True
