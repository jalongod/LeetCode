'''
144. 二叉树的前序遍历
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        if not root:
            return []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res


l1 = TreeNode(1)
# l2 = TreeNode(2)
# l3 = TreeNode(3)
# # l3 = TreeNode(6)
# l1.right = l2
# l2.left = l3

sol = Solution()
max = sol.preorderTraversal(l1)
print(max)
