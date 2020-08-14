'''
86. 分隔链表
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def des(self):
        print(self.val)
        if (self.next is not None):
            self.next.des()


class Solution:
    def partition(self, head: ListNode, x) -> ListNode:
        small_head, big_head = ListNode(0), ListNode(0)
        small_p, big_p = small_head, big_head
        cur = head
        while cur:
            if cur.val < x:
                small_p.next = cur
                small_p = small_p.next
            else:
                big_p.next = cur
                big_p = big_p.next
            cur = cur.next
        big_p.next = None
        small_p.next = big_head.next
        return small_head.next


node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(5)
node6 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sol = Solution()
# node = sol.reverse_linklist(node1)
res = sol.partition(node1, 3)  # 1 2 len(node)
res.des()
