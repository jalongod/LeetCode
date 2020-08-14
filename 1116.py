'''
假设有这么一个类：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

 

示例 1：

输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。

'''
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semaphore1 = threading.Semaphore(1)
        self.semaphore2 = threading.Semaphore(0)
        self.semaphore3 = threading.Semaphore(0)

    def zero(self, printNumber) -> None:
        for i in range(1, self.n + 1):
            self.semaphore1.acquire()
            printNumber(0)
            if i & 1:
                self.semaphore2.release()
            else:
                self.semaphore3.release()

    def even(self, printNumber) -> None:
        for i in range(1, self.n + 1, 2):
            self.semaphore2.acquire()
            printNumber(i)
            self.semaphore1.release()

    def odd(self, printNumber) -> None:
        for i in range(2, self.n + 1, 2):
            self.semaphore3.acquire()
            printNumber(i)
            self.semaphore1.release()

    pass


class ZeroEvenOdd2:
    def __init__(self, n):
        self.n = n
        self.iseven = self.n & 1
        self.oedge = self.n - 1 if self.iseven else self.n
        self.eedge = self.n - 1 if not self.iseven else self.n
        self.index = 0
        self.con = threading.Condition()
        self.next = 'zero'

    def zero(self, printNumber) -> None:
        while (self.index < self.n):
            with self.con:
                if self.next != 'zero':
                    self.con.wait()
                printNumber(0)
                self.index += 1
                if self.index & 1:  # 奇数
                    self.next = 'even'
                else:
                    self.next = 'odd'
                self.con.notify_all()

    def even(self, printNumber) -> None:
        while (self.index < self.eedge):
            with self.con:
                if self.next != 'even':
                    self.con.wait()
                printNumber(self.index)
                self.next = 'zero'
                self.con.notify_all()

    def odd(self, printNumber) -> None:
        while (self.index < self.oedge):
            with self.con:
                if self.next != 'odd':
                    self.con.wait()
                printNumber(self.index)
                self.next = 'zero'
                self.con.notify_all()


def _printNumber(x):
    print(str(x))
    pass


foo = ZeroEvenOdd2(2)
thrs = list()
thrs.append(threading.Thread(target=foo.zero, args=(_printNumber, )))
thrs.append(threading.Thread(target=foo.even, args=(_printNumber, )))
thrs.append(threading.Thread(target=foo.odd, args=(_printNumber, )))

for th in thrs:
    th.start()

for th in thrs:
    th.join()