'''
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:# 递归
#     res = []

#     def inorderTraversal(self, root: TreeNode):
#         if not root:
#             return
#         self.inorderTraversal(root.left)
#         self.res.append(root.val)
#         self.inorderTraversal(root.right)
#         return self.res


class Solution:  # 栈
    def inorderTraversal(self, root: TreeNode):
        res, stack = [], []
        if not root:
            return res
        stack.append(root)
        while len(stack) > 0:
            top = stack[len(stack) - 1]
            if top.left:
                stack.append(top.left)
                continue
            top = stack.pop()
            res.append(top.val)
            if top.right:
                stack.append(top.right)
        return res


l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
# l3 = TreeNode(6)
l1.right = l3
l1.left = l2

sol = Solution()
max = sol.inorderTraversal(l1)
print(max)
