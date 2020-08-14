#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB) -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        res = None
        if not headA or not headB:
            return res
        que1 = []
        que2 = []
        while headA:
            que1.append(headA)
            headA = headA.next
        while headB:
            que2.append(headB)
            headB = headB.next
        node1, node2 = que1.pop(-1), que2.pop(-1)
        while node1.val == node2.val:
            res = node1
        return res


# @lc code=end
