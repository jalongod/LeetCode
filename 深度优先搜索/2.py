#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 打印单链表

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.l3 = None
        self.tail = None
        self.recur(l1, l2, self.l3, 0)
        return self.l3

    # 递归
    def recur(self, l1: ListNode, l2: ListNode, l3: ListNode, fit):
        # terminator
        if (not l1 and not l2 and fit == 0):
            return
        # process
        val1 = 0 if not l1 else l1.val
        val2 = 0 if not l2 else l2.val

        val = val1 + val2 + fit
        plus = val % 10
        new_fit = int(val / 10)

        nnode = ListNode(plus)

        if not self.l3:
            self.l3 = nnode
            self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode

        # drill down
        self.recur(None if not l1 else l1.next, None if not l2 else l2.next, nnode, new_fit)
        # reset
        pass

    def print_list(self, l1: ListNode):
        if not l1:
            return
        print(str(l1.val)+'->')
        self.print_list(l1.next)


if __name__ == '__main__':
    l1 = ListNode(5)
    # l2 = ListNode(4)
    # l3 = ListNode(3)
    # l1.next = l2
    # l2.next = l3

    n1 = ListNode(5)
    # n2 = ListNode(6)
    # n3 = ListNode(4)
    # n1.next = n2
    # n2.next = n3

    sol = Solution()
    max = sol.addTwoNumbers(l1, n1)
    sol.print_list(max)
