# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if not p.val == q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(1)
    l1.left = l2 
    
    l3 = TreeNode(1)
    l4 = TreeNode(1)
    l3.right = l4

    sol = Solution()
    max = sol.isSameTree(l1, l1)
    print(max)
    # sol.print_list(max)
