# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isValidBST(self, root: TreeNode):     
        self.res = []
        self._dfs(root)
        return self.res == sorted(self.res) and len(set(self.res)) == len(self.res)

    def _dfs(self, node: TreeNode):
        if not node:
            return 
        self._dfs(node.left)
        self.res.append(node.val)
        self._dfs(node.right)


if __name__ == '__main__':
    l1 = TreeNode(7)
    l2 = TreeNode(4)
    l3 = TreeNode(8)
    l1.left = l2 
    l1.right = l3
    # l4 = TreeNode(11)
    # l2.left = l4
    # l5 = TreeNode(13)
    # l3.left = l5    
    # l6 = TreeNode(4)
    # l3.right = l6
    # l7 = TreeNode(7)
    # l4.left = l7
    # l8 = TreeNode(2)
    # l4.right = l8
    # l9 = TreeNode(5)
    # l6.left = l9
    # l10 = TreeNode(1)
    # l6.right = l10

    sol = Solution()
    max = sol.isValidBST(l1)
    print(max)
    # sol.print_list(max)
