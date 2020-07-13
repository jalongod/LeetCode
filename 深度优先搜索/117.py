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
            return root
        queue = [root]
        while (queue):
            node_pre = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node_pre:
                    node_pre.next = node
                node_pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


if __name__ == '__main__':
    l4 = Node(4, None, None, None)
    l5 = Node(5, None, None, None)
    l7 = Node(7, None, None, None)
    l2 = Node(2, l4, l5, None)
    l3 = Node(3, None, l7, None)
    l1 = Node(1, l2, l3, None)

    sol = Solution()
    max = sol.connect(l1)
    sol.print_list(max)
