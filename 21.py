'''
21. 合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def mergeTwoLists2(self, l1, l2):
        res, tail = None, None

        def merge(l1, l2):
            nonlocal res, tail
            if not l1 and not l2:
                return
            if not l1 or (l2 and l1.val >= l2.val):
                if not res:
                    res = ListNode(l2.val)
                    tail = res
                else:
                    tail.next = ListNode(l2.val)
                    tail = tail.next
                merge(l1, l2.next)
            else:
                if not res:
                    res = ListNode(l1.val)
                    tail = res
                else:
                    tail.next = ListNode(l1.val)
                    tail = tail.next
                merge(l1.next, l2)

        merge(l1, l2)
        return res


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
res = sol.mergeTwoLists(node1, n1)
print(res)