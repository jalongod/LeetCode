# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None
        if not len(preorder) == len(inorder):
            return None

        def build(l1, l2) -> TreeNode:
            if len(l1) <= 0:
                return None
            head = TreeNode(l1[0])
            if len(l1) == 1:
                return head
            loc = l2.index(head.val)

            head.left = build(l1[1:loc + 1], l2[0:loc])
            head.right = build(l1[loc + 1:len(l2)], l2[loc + 1:len(l2)])
            return head

        res = build(preorder, inorder)
        return res


if __name__ == '__main__':

    sol = Solution()
    max = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    # max = sol.buildTree([1, 2], [2, 1])
    # max = sol.buildTree([1, 2, 3], [2, 3, 1])

    print(max)
    # sol.print_list(max)
