import threading


def async_task_with_threading(*args):
    def sleeper():
        import time
        time.sleep(5)

    t = threading.Thread(target=sleeper, args=(args,))
    t.start()
