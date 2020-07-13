#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (37.39%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 20.4K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# 输出:
#
#
# 2
#
#
# 示例 2:
#
# 输入:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# 输出:
#
#
# 2
#
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
#
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def dfs(self, node):
        if not node or (not node.left and not node.right):
            return 0
        lval, rval = 0, 0
        lval = self.dfs(node.left)
        rval = self.dfs(node.right)

        leftheight, rightheight = 0, 0
        if node.left and node.left.val == node.val:
            leftheight += lval + 1
        if node.right and node.right.val == node.val:
            rightheight += rval + 1
        self.res = max(self.res, leftheight + rightheight)
        return max(leftheight, rightheight)

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res


# @lc code=end

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
l3.left = l6
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
