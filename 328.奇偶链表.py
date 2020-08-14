# 至少写五遍
#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
# https://leetcode-cn.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (59.50%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 33.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
#
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
# 说明:
#
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd, even = ListNode(0), ListNode(0)
        ot, et = odd, even
        flag = True
        p = head
        while p:
            if flag:
                ot.next = p
                ot = ot.next
            else:
                et.next = p
                et = et.next
            flag = not flag
            p = p.next
        ot.next = even.next
        et.next = None
        return odd.next


# @lc code=end

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
sol = Solution()
n6 = sol.oddEvenList(n1)
print(n6)
