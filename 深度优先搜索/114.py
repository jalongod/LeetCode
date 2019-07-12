# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        将已经flat化的左子树A作为root的右孩子，将flat化root原右孩子作为A最右孩子的右孩子，中间将节点的做孩子置为null
        """

        def flat(root: TreeNode) -> TreeNode:
            if not root:
                return
            right = root.right
            fl = flat(root.left)
            root.right = fl
            root.left = None
            while fl and fl.right:
                fl = fl.right
            if fl:
                fl.right = flat(right)
            else:
                root.right = flat(right)
            return root

        flat(root)
        print(root)


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
    max = sol.flatten(l1)
    sol.print_list(max)
