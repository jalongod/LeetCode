'''
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。 

'''
# Definition for a Node.


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    cache = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if head in self.cache:
            return self.cache[head]
        res = Node(head.val, None, None)
        self.cache[head] = res
        res.next = self.copyRandomList(head.next)
        res.random = self.copyRandomList(head.random)
        return res


node1 = Node(1, None, None)
node2 = Node(2, None, None)
node3 = Node(3, None, None)
node4 = Node(4, None, None)
node1.next = node2
node2.next = node3
node3.next = node4
node2.random = node4
node4.random = node2

sol = Solution()
res = sol.copyRandomList(node1)
print(res)
