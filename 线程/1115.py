'''
我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-foobar-alternately
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from threading import Thread, Condition, Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.semaphore1 = Semaphore(0)
        self.semaphore2 = Semaphore(1)

    def foo(self, printFoo) -> None:

        for i in range(self.n):
            self.semaphore2.acquire()
            printFoo()
            self.semaphore1.release()

    def bar(self, printBar) -> None:

        for i in range(self.n):
            self.semaphore1.acquire()
            printBar()
            self.semaphore2.release()


class FooBar2:
    def __init__(self, n):
        self.n = n
        self.val = 'foo'
        self.con = Condition()

    def foo(self, printFoo) -> None:

        for i in range(self.n):
            with self.con:
                if self.val != 'foo':
                    print("wait 前")
                    self.con.wait()
                    print("wait 后")
                printFoo()
                self.val = 'bar'
                self.con.notify_all()

    def bar(self, printBar) -> None:

        for i in range(self.n):
            with self.con:
                if self.val == 'foo':
                    self.con.wait()
                printBar()
                self.val = 'foo'
                self.con.notify_all()


def _printFoo():
    print('foo', end='')


def _printBar():
    print('bar')


foo = FooBar2(10)
thrs = list()
thrs.append(Thread(target=foo.foo, args=(_printFoo, )))
thrs.append(Thread(target=foo.bar, args=(_printBar, )))

for th in thrs:
    th.start()

for th in thrs:
    th.join()
