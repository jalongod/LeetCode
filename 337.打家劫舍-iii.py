#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (54.30%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 20.5K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
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
    def rob(self, root: TreeNode) -> int:
        memo = dict()
        return self.subrob(root, memo)

    def subrob(self, root: TreeNode, memo) -> int:
        if not root:
            return 0
        if root in memo:
            return memo[root]
        money = root.val
        if root.left:
            money += self.subrob(root.left.left, memo) + self.subrob(
                root.left.right, memo)
        if root.right:
            money += self.subrob(root.right.left, memo) + self.subrob(
                root.right.right, memo)
        result = max(
            money,
            self.subrob(root.left, memo) + self.subrob(root.right, memo))
        memo.setdefault(root, result)
        return result


# @lc code=end

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
    max = sol.rob(l1)
    print(max)
