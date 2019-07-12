# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self._hasSum(root, sum)

    def _hasSum(self, root: TreeNode, sum: int) -> bool:
        # terminator
        if root and not root.left and not root.right:
            return sum == root.val
        #
        lhas, rhas = False, False
        if root.left:
            lhas = self._hasSum(root.left, sum-root.val)
        if root.right:
            rhas = self._hasSum(root.right, sum-root.val)
        return lhas or rhas


if __name__ == '__main__':
    l1 = TreeNode(5)
    l2 = TreeNode(4)
    l3 = TreeNode(8)
    l1.left = l2 
    # l1.right = l3
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
    max = sol.hasPathSum(l1, 5)
    print(max)
