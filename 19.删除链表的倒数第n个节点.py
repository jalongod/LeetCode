#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (36.11%)
# Likes:    565
# Dislikes: 0
# Total Accepted:    86.5K
# Total Submissions: 239.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, head
        while p2:
            if n > 0:
                p2 = p2.next
                n -= 1
            else:
                p1, p2 = p1.next, p2.next
        p1.next = p1.next.next
        return dummy.next


# @lc code=end

l1 = ListNode(1)
l2 = ListNode(2)
# l1.next = l2
sol = Solution()
sol.removeNthFromEnd(l1, 1)
