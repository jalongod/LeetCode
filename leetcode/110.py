# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     lh = self._getHeight(root.left)
    #     rh = self._getHeight(root.right)
    #     return abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    # def _getHeight(self, node: TreeNode):
    #     if not node:
    #         return 0
    #     lh = self._getHeight(node.left)
    #     rh = self._getHeight(node.right)
    #     return 1+max(lh, rh)
    #     pass
    def isBalanced(self, root: TreeNode) -> bool:
        return not self._depth(root) == -1

    def _depth(self, node):
        if not node:
            return 0
        left = self._depth(node.left)
        if left == -1:
            return -1
        right = self._depth(node.right)
        if right == -1:
            return -1
        return max(left, right)+1 if abs(left - right) <= 1 else -1

if __name__ == '__main__':
    l1 = TreeNode(5)
    l2 = TreeNode(4)
    l3 = TreeNode(8)
    l1.left = l2 
    l1.right = l3

    l4 = TreeNode(11)
    l2.left = l4

    l5 = TreeNode(13)
    l3.left = l5    

    l6 = TreeNode(4)
    l4.right = l6

    # l7 = TreeNode(7)
    # l4.left = l7
    l8 = TreeNode(2)
    l5.right = l8
    # l9 = TreeNode(5)
    # l6.left = l9
    # l10 = TreeNode(1)
    # l6.right = l10

    sol = Solution()
    max = sol.isBalanced(l1)
    print(max)
