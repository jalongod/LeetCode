# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.res = None
        self.head = None
        self._mdfs(root)
        return self.head

    def _mdfs(self, node: TreeNode):
        if not node:
            return
        self._mdfs(node.left)
        if not self.res:
            self.res = node
            self.head = node
        else:
            self.res.right = node
            self.res = self.res.right
        self._mdfs(node.right)


if __name__ == '__main__':
    # [5,3,6,2,4,null,8,1,null,null,null,7,9]
    #         5
    #      3      6
    #    2   4       8
    #  1            7  9 
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l7 = TreeNode(7)
    l8 = TreeNode(8)
    l9 = TreeNode(9)

    l5.left = l3
    l5.right = l6
    l3.left = l2
    l3.right = l4
    l2.left = l1
    l6.right = l8
    l8.left = l7
    l8.right = l9

    # l1.left = l2
    # l1.right = l3

    # n1 = TreeNode(5)
    # n2 = TreeNode(6)
    # n3 = TreeNode(4)
    # n1.left = n2
    # n1.right = n3

    sol = Solution()
    max = sol.increasingBST(l5)
    print(max)