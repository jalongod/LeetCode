'''
687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxLen = 0

    def longestCount(self, root: TreeNode) -> int:
        if not root:
            self.maxLen = max(self.maxLen, 0)
            return 0
        if not root.left and not root.right:
            self.maxLen = max(self.maxLen, 1)
            print(str(root.val) + '=' + str(1))
            return 1

        left = self.longestCount(root.left) if root.left else 0
        right = self.longestCount(root.right) if root.right else 0

        res = 1
        if root.left and root.right and root.left.val == root.val and root.right.val == root.val:
            res += max(left, right)
            self.maxLen = max(self.maxLen, left + right + 1)
        elif root.left and root.left.val == root.val:
            res += left
            self.maxLen = max(self.maxLen, left + 1)
        elif root.right and root.right.val == root.val:
            res += right
            self.maxLen = max(self.maxLen, right + 1)
        else:
            self.maxLen = max(self.maxLen, 1)

        print(str(root.val) + '=' + str(res))
        return res

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longestCount(root)
        return max(self.maxLen - 1, 0)
        pass


if __name__ == '__main__':
    l1 = TreeNode(5)
    l2 = TreeNode(4)
    l3 = TreeNode(5)
    l4 = TreeNode(1)
    l5 = TreeNode(1)
    l6 = TreeNode(5)
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    l3.right = l6

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
    max = sol.longestUnivaluePath(l1)
    print(max)
    # sol.print_list(max)