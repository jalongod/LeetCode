# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        list = []
        queue = [root]
        while queue:
            size = len(queue)
            print(queue[-1].val)
            list.append(queue[-1].val)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return list


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l1.left = l2
    l1.right = l5
    l2.left = l3
    l2.right = l4
    l5.right = l6

    sol = Solution()
    max = sol.rightSideView(l1)
    sol.print_list(max)
