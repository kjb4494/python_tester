import asyncio
import threading
import time
import queue
from decorators import limited_thread, time_measurement


lock = threading.Lock()
loop = asyncio.get_event_loop()


async def async_test(num, i):
    print('start ' + str(num) + ' thread: ' + str(i) + 'async loop!')
    await loop.run_in_executor(None, time.sleep, 3)
    print('finished ' + str(num) + ' thread: ' + str(i) + 'async loop!')


@limited_thread
def threading_test(num):
    print(str(num).zfill(2) + ' threading start!')
    time.sleep(5)
    print(str(num).zfill(2) + ' threading middle finished!')
    futures = [async_test(num, i) for i in range(50)]
    with lock:
        loop.run_until_complete(asyncio.wait(futures))
    print(str(num).zfill(2) + ' threading finished!')


@time_measurement
def main_module():
    thread_count = 10
    threads = queue.Queue()
    for i in range(thread_count):
        th = threading.Thread(target=threading_test, args=(i,))
        threads.put(th)
        th.start()
    for _ in range(thread_count):
        threads.get().join()


if __name__ == '__main__':
    main_module()
