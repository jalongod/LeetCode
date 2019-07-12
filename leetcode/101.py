# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        return self._isSym(root, root)
    
    def _isSym(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self._isSym(p.left, q.right) and self._isSym(p.right, q.left) and p.val == q.val


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l1.left = l2
    
    l3 = TreeNode(1)
    l4 = TreeNode(1)
    l3.right = l4

    sol = Solution()
    max = sol.isSymmetric(l1)
    print(max)
    # sol.print_list(max)
