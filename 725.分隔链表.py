#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#
# https://leetcode-cn.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (50.52%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 7.7K
# Testcase Example:  '[1,2,3,4]\n5'
#
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
# 返回一个符合上述规则的链表的列表。
#
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
#
# 示例 1：
#
#
# 输入:
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且
# root.next.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
#
#
# 示例 2：
#
#
# 输入:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
#
#
#
#
# 提示:
#
#
# root 的长度范围： [0, 1000].
# 输入的每个节点的大小范围：[0, 999].
# k 的取值范围： [1, 50].
#
#
#
#
#

from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res, length, head = [], 0, root
        while head or length < k:
            if head:
                head = head.next
            length += 1
        size, tail, i = length // k, length % k, 0
        lens = [size for _ in range(k)]  # 第i个链表的长度
        while i < tail:
            lens[i] += 1
            i += 1
        head, index = root, 0
        while index < k:
            length, tail = lens[index], None
            while length:
                node = ListNode(head.val) if head else None
                if len(res) == index:
                    res.append(node)
                    tail = node
                else:
                    tail.next = node
                    tail = tail.next
                length -= 1
                if head:
                    head = head.next
            index += 1
        return res

        pass


# @lc code=end

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = n7
# n7.next = n8
sol = Solution()
n6 = sol.splitListToParts(n1, 5)
print(n6)