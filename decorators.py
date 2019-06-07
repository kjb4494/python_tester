import threading
import time


def limited_thread(func):
    sem = threading.Semaphore(5)

    def wrapper(*args, **kwargs):
        sem.acquire()
        order = func(*args, **kwargs)
        sem.release()
        return order

    return wrapper


def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        order = func(*args, **kwargs)
        print('--- {} seconds ---'.format(time.time() - start_time))
        return order

    return wrapper
