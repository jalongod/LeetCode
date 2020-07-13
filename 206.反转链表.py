#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (65.25%)
# Likes:    639
# Dislikes: 0
# Total Accepted:    118.2K
# Total Submissions: 180.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 迭代
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head
    #     pre, cur = None, head
    #     while cur:
    #         nex = cur.next
    #         cur.next = pre
    #         pre = cur
    #         cur = nex
    #     return pre

    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head  # 重要
        head.next = None  # 十分重要
        return res


# @lc code=end

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
sol = Solution()
n6 = sol.reverseList(n1)
print(n6)
