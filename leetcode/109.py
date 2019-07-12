# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        self.head = head
        idx = 0
        while head:
            idx += 1
            head = head.next

        def sort(left, right):
            if left > right:
                return
            m = (left + right) >> 1

            #左子树
            left_node = sort(left, m - 1)

            node = TreeNode(self.head.val)
            node.left = left_node

            self.head = self.head.next
            #右子树
            node.right = sort(m + 1, right)
            return node

        return sort(0, idx - 1)


if __name__ == '__main__':

    node1 = ListNode(-10)
    node2 = ListNode(-3)
    node3 = ListNode(0)
    node4 = ListNode(5)
    node5 = ListNode(9)
    node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node5
    sol = Solution()
    max = sol.sortedListToBST(node1)

    print(max)
    # sol.print_list(max)