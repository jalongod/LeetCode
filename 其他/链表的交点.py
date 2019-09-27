'''
寻找两个单项链表的交点
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 在确认有交点的情况下，查找两个链表的交点 用栈 或者比较长度
    def findJiaoDian(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

    # 查找两个链表是否有交点 用栈
    def checkJiaoDian(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

n1 = ListNode(1)
n2 = ListNode(2)
# n4 = ListNode(4)
n1.next = n2
n2.next = node3
sol = Solution()
# res = sol.mergeKLists([node1, n1])
res = sol.findJiaoDian(node1, n1)
print(res.val)
