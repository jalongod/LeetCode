#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (39.00%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    46.5K
# Total Submissions: 119K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # empty
        if not head or not head.next:
            return True
        p1, p2, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            p3, p2.next = p2.next, p1
            p1, p2 = p2, p3
        if fast:
            p2 = p2.next
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        return p1 is None


# @lc code=end

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(2)
n6 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
sol = Solution()
n6 = sol.isPalindrome(n1)
print(n6)
