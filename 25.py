'''
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_linklist(self, head) -> ListNode:  # 需要背过
        p1, p2 = None, head
        while (p2):
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        return p1

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        pre_head = ListNode(0)
        pre_head.next = head

        pre, end = pre_head, pre_head
        while (end.next):
            index = 0
            while (index < k and end):
                end, index = end.next, index + 1
            if not end:
                break
            # 反转 pre 到tail
            start = pre.next
            next = end.next
            end.next = None  # 关键
            pre.next = self.reverse_linklist(start)
            start.next = next
            # pre tail = 最后一个
            pre, end = start, start
        return pre_head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
# node = sol.reverse_linklist(node1)
res = sol.reverseKGroup(node1, 2)  # 1 2 len(node)
print(res)
