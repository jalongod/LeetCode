# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


if __name__ == '__main__':
    l4 = Node(4, None, None, None)
    l5 = Node(5, None, None, None)
    l6 = Node(6, None, None, None)
    l7 = Node(7, None, None, None)
    l2 = Node(2, l4, l5, None)
    l3 = Node(3, l6, l7, None)
    l1 = Node(1, l2, l3, None)

    sol = Solution()
    max = sol.connect(l1)
    sol.print_list(max)
