# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = float("-inf")

        # 获取该节点以及其子树的最大贡献
        def getSum(node: TreeNode):
            nonlocal maxSum

            if not node:
                return 0
            lsum = max(getSum(node.left), 0)
            rsum = max(getSum(node.right), 0)
            maxSum = max(maxSum, lsum + rsum + node.val)
            print('sum = ' + str(maxSum))
            return max(lsum, rsum) + node.val

        getSum(root)
        return maxSum
        pass


if __name__ == '__main__':
    # l1 = TreeNode(1)
    # l2 = TreeNode(2)
    # l3 = TreeNode(3)
    # l4 = TreeNode(4)
    # l5 = TreeNode(5)
    # l6 = TreeNode(6)
    # l1.left = l2
    # l1.right = l5
    # l2.left = l3
    # l2.right = l4
    # l5.right = l6

    l1 = TreeNode(-10)
    l2 = TreeNode(90)
    l3 = TreeNode(20)
    l4 = TreeNode(15)
    l5 = TreeNode(7)
    l1.left = l2
    l1.right = l3
    l3.left = l4
    l3.right = l5

    sol = Solution()
    max = sol.maxPathSum(l1)
    print(max)
