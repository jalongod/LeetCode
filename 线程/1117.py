'''
1117. H2O 生成

现在有两种线程，氢 oxygen 和氧 hydrogen，你的目标是组织这两种线程来产生水分子。
存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。
氢和氧线程会被分别给予 releaseHydrogen 和 releaseOxygen 方法来允许它们突破屏障。
这些线程应该三三成组突破屏障并能立即组合产生一个水分子。
你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。
换句话说:

如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
书写满足这些限制条件的氢、氧线程同步代码。

 

示例 1:

输入: "HOH"
输出: "HHO"
解释: "HOH" 和 "OHH" 依然都是有效解。
示例 2:

输入: "OOHHHH"
输出: "HHOHHO"
解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。
 

限制条件:

输入字符串的总长将会是 3n, 1 ≤ n ≤ 50；
输入字符串中的 “H” 总数将会是 2n；
输入字符串中的 “O” 总数将会是 n。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/building-h2o
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from threading import Thread, Condition, Semaphore, Lock


class H2O:
    def __init__(self):
        self.con = Condition()
        self.hc = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.con:
            # 如果hc等于2，就等待
            if self.hc == 2:
                self.con.wait()
            # 当hc不等于2的时候：打印、累加、通知
            releaseHydrogen()
            self.hc += 1
            self.con.notify_all()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.con:
            if self.hc != 2:
                self.con.wait()
            releaseOxygen()
            self.hc = 0
            self.con.notify_all()


class H2O2:
    def __init__(self):
        self.sem1 = Semaphore(2)  # 两个H
        self.sem2 = Semaphore(1)  # 一个O

        self.sem3 = Semaphore(0)
        self.sem4 = Semaphore(0)
        pass

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sem1.acquire()  # 保证两个H线程进入
        self.sem3.release()  # 释放H原子到达的信号
        self.sem4.acquire()  # 等待O到达
        releaseHydrogen()
        self.sem1.release()  # 唤醒一个H线程

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sem2.acquire()  # 保证一个O线程进入
        self.sem4.release()  # 释放o原子到达信号，因为有两个H线程等待，所以释放两个信号
        self.sem4.release()
        self.sem3.acquire()  # 等待H到达
        self.sem3.acquire()
        releaseOxygen()
        self.sem2.release()


def _releaseH():
    print('H')
    pass


def _releaseO():
    print('O')
    pass


foo = H2O()
thrs = list()
inputs = "OOHHHH"
for char in inputs:
    if char == 'O':
        thrs.append(Thread(target=foo.oxygen, args=(_releaseO, )))
    else:
        thrs.append(Thread(target=foo.hydrogen, args=(_releaseH, )))

for th in thrs:
    th.start()

for th in thrs:
    th.join()