'''
61. 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针找到须断开的节点的前一个节点n1和尾结点n2
    # n2与头结点相连
    # n1.next 是返回值
    # n1.next = None
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        # 计算链表长度
        node = head
        length = 0
        while (node):
            node = node.next
            length += 1
        step = k % length
        if step == 0:
            return head
        p1, p2, inter = head, head, 0
        while (p2.next):
            p2 = p2.next
            if inter >= step:
                p1 = p1.next
            inter += 1
        p2.next, res, p1.next = head, p1.next, None
        return res


node1 = ListNode(1)
node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

sol = Solution()
# node = sol.reverse_linklist(node1)
res = sol.rotateRight(node1, 2)  # 1 2 len(node)
print(res)
