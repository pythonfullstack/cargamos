from celery import Celery

celery_app = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@celery_app.task
def task_with_celery():
    import time
    time.sleep(3)
    return True
