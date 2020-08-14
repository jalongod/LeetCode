'''
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next

    def swapPairs_while(self, head: ListNode) -> ListNode:
        pre_head = ListNode(0)
        pre_head.next = head
        temp = pre_head
        while (temp.next and temp.next.next):
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        return pre_head.next

    def swapPair_recur(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        end = head.next
        head.next = self.swapPair_recur(end.next)
        end.next = head
        return end


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

# n1 = ListNode(1)
# n2 = ListNode(3)
# n3 = ListNode(4)
# n1.next = n2
# n2.next = n3
sol = Solution()
# res = sol.mergeKLists([node1, n1])
res = sol.swapPair_recur(node1)
print(res)
