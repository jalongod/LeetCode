'''
23. 合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode,
                      l2: ListNode) -> ListNode:  # leetcode 21
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def mergeKLists(self, lists) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None


node1 = ListNode(1)
node2 = ListNode(2)
# node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node4
# node3.next = node4

n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
n1.next = n2
n2.next = n3
sol = Solution()
# res = sol.mergeKLists([node1, n1])
res = sol.mergeKLists([])
print(res)