#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

' 单链表反转 '
__author__ = 'zcr'


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def des(self):
        print(self.value)
        if (self.next is not None):
            self.next.des()


def reverse(head):
    if (head is None) or (head.next is None):
        return head
    p1 = head
    p2 = head.next
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
        pass
    head.next = None
    return p1


if __name__ == '__main__':
    node1 = Node('1', None)
    node2 = Node('2', node1)
    node3 = Node('3', node2)
    node4 = Node('4', node3)
    node4.des()
    print('began to reverse ')
    noder = reverse(node4)
    print('success to reverse ')
    noder.des()
