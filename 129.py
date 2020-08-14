# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum = 0

        def _dfs(node: TreeNode, num):
            nonlocal sum
            if not node:
                return
            # process

            num = num * 10 + node.val
            if not node.left and not node.right:
                print('num=' + str(num))
                sum += num
                return

            _dfs(node.left, num)
            _dfs(node.right, num)
            pass

        _dfs(root, 0)
        return sum


if __name__ == '__main__':
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    l1.left = l2
    l1.right = l3
    # l2.left = l3
    # l2.right = l4
    # l5.right = l6

    sol = Solution()
    max = sol.sumNumbers(l1)
    print(max)
