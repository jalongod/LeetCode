#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (52.47%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 20K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 迭代 超时了
        if not head or not head.next:
            return head

        def reverse(node):  # 反转链表
            if not node:
                return node
            p1, p2 = None, node
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                pass
            return p1
        # while(head):
        #     head.next = reverse(head.next)
        #     head = head.next
        # return head

        # 将链表加入到数组中，重排

        # 将链表分为前后两部分，后半部分反转
        def reverse(node):  # 反转链表
            if not node:
                return node
            p1, p2 = None, node
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                pass
            return p1
        length, h1, h2, h3 = 0, head, head, head
        while h1:
            length += 1
            h1 = h1.next
        mid = length/2-1
        while mid > 0:
            mid -= 1
            h2 = h2.next
        tail = reverse(h2.next)
        h2.next = None

        while (tail and h3):
            h3_tmp = h3.next
            tail_tmp = tail.next

            tail.next = h3.next
            h3.next = tail
            tail.next

            tail = tail_tmp
            h3 = h3_tmp
        return head
        # @lc code=end


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5
sol = Solution()
n6 = sol.reorderList(n1)
print(n6)
