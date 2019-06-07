from threading import Thread, Lock


class ThreadTester:
    def __init__(self):
        self.lock = Lock()
        self._value = 0

    def value_add_with_lock(self, num):
        for _ in range(num):
            with self.lock:
                self._value += 1

    def value_sub_with_lock(self, num):
        for _ in range(num):
            with self.lock:
                self._value -= 1

    def value_add(self, num):
        for _ in range(num):
            self._value += 1

    def value_sub(self, num):
        for _ in range(num):
            self._value -= 1

    def get_value(self):
        return self._value


if __name__ == '__main__':
    tester = ThreadTester()
    th1 = Thread(target=tester.value_add, args=(5000000, ))
    th2 = Thread(target=tester.value_sub, args=(5000000, ))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('no lock: ' + str(tester.get_value()))

    tester = ThreadTester()
    th1 = Thread(target=tester.value_add_with_lock, args=(5000000,))
    th2 = Thread(target=tester.value_sub_with_lock, args=(5000000,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print('with lock: ' + str(tester.get_value()))
