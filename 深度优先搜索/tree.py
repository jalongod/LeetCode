'''
# 通过代码将以下二叉树输出结果：ACBGFEDH

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bfs(self, root: TreeNode):
        queue = list()
        queue.append(root)
        while (queue):
            node = queue.pop(0)
            if node:
                print(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            pass
        pass


if __name__ == '__main__':
    l1 = TreeNode("a")
    l2 = TreeNode("b")
    l3 = TreeNode("c")
    l4 = TreeNode("d")
    l5 = TreeNode("e")
    l6 = TreeNode("f")
    l7 = TreeNode("g")
    l8 = TreeNode("h")
    l1.left = l2
    l1.right = l3
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7
    l4.left = l8

    sol = Solution()
    max = sol.bfs(l1)
    print(max)