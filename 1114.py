import threading


class Foo(object):
    semaphore1 = threading.Semaphore(0)
    semaphore2 = threading.Semaphore(0)

    def first(self):
        print("first" + '\n')
        self.semaphore1.release()

    def second(self):
        self.semaphore1.acquire()
        print("second" + '\n')
        self.semaphore2.release()

    def third(self):

        self.semaphore2.acquire()
        print("third" + '\n')


class Foo2(object):
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def first(self):
        self.lock1.acquire()
        print("first" + '\n')
        self.lock1.release()

    def second(self):
        self.lock1.acquire()
        print("second" + '\n')
        self.lock2.release()

    def third(self):
        self.lock1.acquire()
        self.lock2.acquire()
        print("third" + '\n')


if __name__ == '__main__':
    sol = Foo2()
    t1 = threading.Thread(target=sol.first)
    t2 = threading.Thread(target=sol.second)
    t3 = threading.Thread(target=sol.third)
    t3.start()
    t2.start()
    t1.start()
