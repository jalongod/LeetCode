#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (62.47%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 46.8K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from queue import PriorityQueue


class Solution:
    # 优先队列
    # def sortList(self, head: ListNode) -> ListNode:
    #     pq = PriorityQueue()
    #     h1 = head
    #     while h1:
    #         pq.put(h1.val)
    #         h1 = h1.next
    #     h1 = head
    #     while not pq.empty():
    #         h1.val = pq.get()
    #         h1 = h1.next
    #     return head

    # 列表法
    def sortList(self, head: ListNode) -> ListNode:
        l1 = []
        h1 = head
        while h1:
            l1.append(h1.val)
            h1 = h1.next
        l1.sort()
        h1 = head
        for i in range(len(l1)):
            h1.val = l1[i]
            h1 = h1.next
        return head


# @lc code=end
