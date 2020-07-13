#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (62.98%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    32.9K
# Total Submissions: 52K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其自底向上的层次遍历为：
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
# from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue, head = [], [], root
        queue.append(head)
        while queue:
            lsize = len(queue)
            larr = []
            for i in range(lsize):
                node = queue.pop(0)
                if node:
                    larr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if len(larr):
                res.insert(0, larr)
        return res


# @lc code=end

# [3, 9, 20, null, null, 15, 7]
l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)
l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5

sol = Solution()
sol.levelOrderBottom(l1)
