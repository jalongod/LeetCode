'''
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        p1, p2, length = None, head, 0
        # 获取须删除的前一个节点:p1
        while (p2):
            p2 = p2.next
            if length < n:
                length += 1
            elif not p1:
                p1 = head
            else:
                p1 = p1.next
        # 删除节点p1
        if not p1:
            head = head.next
        elif p1.next.next:
            p1.next.val = p1.next.next.val
            p1.next = p1.next.next
        else:
            p1.next = None
        return head

    pass


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
res = sol.removeNthFromEnd(node1, 2)
print(res)
