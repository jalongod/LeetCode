# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.leefs1 = []
        self.leefs2 = []
        self._dfs(root1, self.leefs1) 
        self._dfs(root2, self.leefs2)
        return self.leefs1 == self.leefs2

    def _dfs(self, node: TreeNode, leefs):
        if not node:
            return 
        if not node.left and not node.right:
            leefs.append(node.val)
            return
        self._dfs(node.left, leefs)
        self._dfs(node.right, leefs)


if __name__ == '__main__':
    l1 = TreeNode(5)
    l2 = TreeNode(6)
    l3 = TreeNode(4)
    # l1.left = l2
    # l1.right = l3

    n1 = TreeNode(5)
    n2 = TreeNode(6)
    n3 = TreeNode(4)
    # n1.left = n2
    # n1.right = n3

    sol = Solution()
    max = sol.leafSimilar(l1, n1)
    print(max)