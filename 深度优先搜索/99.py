# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.pre = TreeNode(float("-inf"))
        self._dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def _dfs(self, node):
        if not node:
            return
        self._dfs(node.left)
        if not self.first and self.pre.val >= node.val:
            self.first = self.pre
        if self.first and self.pre.val >= node.val:
            self.second = node
        self.pre = node
        self._dfs(node.right)
        pass


if __name__ == '__main__':
    l3 = TreeNode(3)
    l1 = TreeNode(1)
    l4 = TreeNode(4)
    l2 = TreeNode(2)
    l3.left = l1
    l3.right = l4
    l4.left = l2
    sol = Solution()
    max = sol.recoverTree(l3)
    print(max)
    # sol.print_list(max)
