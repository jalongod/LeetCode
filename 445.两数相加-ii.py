#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (51.58%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 17.6K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
#
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 进阶:
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
# 示例:
#
#
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
#
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 暴力求解
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     h1, h2 = l1, l2
    #     v1 = 0
    #     v2 = 0
    #     while h1:
    #         v1 = v1 * 10 + h1.val
    #         h1 = h1.next
    #     while h2:
    #         v2 = v2 * 10 + h2.val
    #         h2 = h2.next
    #     v3 = v1 + v2
    #     dummy = ListNode(0)

    #     if v3 == 0:
    #         return dummy
    #     # 头插法
    #     while v3 > 0:
    #         vt = v3 % 10
    #         v3 = v3 // 10
    #         n3 = ListNode(vt)
    #         n3.next = dummy.next
    #         dummy.next = n3
    #     return dummy.next

    # 先计算两个链表的长度
    # 然后对短链表前面补0 两个链表长度相同
    # 使用递归先计算最末尾节点 利用递归的回溯特性 不断更新carry进位与新的结果头节点
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre1, pre2 = ListNode(0), ListNode(0)
        pre1.next, pre2.next = l1, l2
        h1, h2 = l1, l2
        # 补零
        while h1 or h2:
            if not h1:
                node = ListNode(0)
                node.next = pre1.next
                pre1.next = node
            elif not h2:
                node = ListNode(0)
                node.next = pre2.next
                pre2.next = node
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
        dummy = ListNode(0)

        def dfs(l1, l2):
            if not l1 and not l2:
                return False
            jw1 = dfs(l1.next, l2.next)
            v2 = l1.val + l2.val + 1 if jw1 else l1.val + l2.val
            node = ListNode(v2 % 10)
            node.next = dummy.next
            dummy.next = node
            return v2 // 10 > 0

        if dfs(pre1.next, pre2.next):
            node = ListNode(1)
            node.next = dummy.next
            dummy.next = node
        return dummy.next


# @lc code=end

n1 = ListNode(3)
n2 = ListNode(3)
# n3 = ListNode(3)

n4 = ListNode(3)
n5 = ListNode(3)
# n6 = ListNode(6)
n1.next = n2
# n2.next = n3

n4.next = n5
# n5.next = n6
sol = Solution()
n6 = sol.addTwoNumbers(n1, n4)
print(n6)
