# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if len(inorder) <= 0 or len(postorder) <= 0:
            return None
        if not len(inorder) == len(postorder):
            return None

        def build(l1, l2) -> TreeNode:
            if len(l1) <= 0:
                return
            if len(l1) == 1:
                return TreeNode(l1[0])
            head = TreeNode(l2[-1])
            loc = l1.index(head.val)

            head.left = build(l1[:loc], l2[:loc])
            head.right = build(l1[loc + 1:], l2[loc:len(l2) - 1])
            return head

        res = build(inorder, postorder)
        return res


if __name__ == '__main__':

    sol = Solution()
    max = sol.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    # max = sol.buildTree([1, 2], [2, 1])
    # max = sol.buildTree([1, 2, 3], [2, 3, 1])

    print(max)
    # sol.print_list(max)
