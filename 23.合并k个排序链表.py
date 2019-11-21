#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (47.71%)
# Likes:    374
# Dislikes: 0
# Total Accepted:    51.9K
# Total Submissions: 108.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# @lc code=start
# Definition for singly-linked list.
from typing import List
from queue import PriorityQueue
from heapq import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 优先队列
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq, (lists[i].val, i))
                lists[i] = lists[i].next
        res = ListNode(0)
        tail = res
        while pq:
            val, idx = heappop(pq)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[idx]:
                heappush(pq, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return res.next


# @lc code=end

l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(5)
l1.next = l2
l2.next = l3

ll1 = ListNode(1)
ll2 = ListNode(3)
ll3 = ListNode(4)
ll1.next = ll2
ll2.next = ll3

sol = Solution()
sol.mergeKLists([l1, ll1])
