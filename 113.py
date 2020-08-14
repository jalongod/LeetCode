# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        self.ret = []
        self._dfs(root, [], sum)
        return self.ret
        pass

    # def pathSum(self, root: TreeNode, sum: int):
    #     res = []
    #     if not root: return []
    #     def helper(root,sum, tmp):
    #         if not root:
    #             return
    #         if not root.left and not root.right and sum - root.val == 0 :
    #             tmp += [root.val]
    #             res.append(tmp)
    #             return
    #         helper(root.left, sum - root.val, tmp + [root.val])
    #         helper(root.right, sum - root.val, tmp + [root.val])
    #     helper(root, sum, [])
    #     return res

    def _dfs(self, node: TreeNode, path, min):
        if not node:
            return
        if not node.left and not node.right and min == node.val:
            print(path)
            # 根节点
            path += [node.val]
            # path.append(node.val)
            self.ret.append(path)
            return
        # process
        # path.append(node.val)
        # min -= node.val
        # drill down
        # self._dfs(node.left,path,min)
        # self._dfs(node.right,path,min)
        self._dfs(node.left, path + [node.val], min - node.val)
        self._dfs(node.right, path + [node.val], min - node.val)
        pass


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
    l3.right = l6
    l7 = TreeNode(7)
    l4.left = l7
    l8 = TreeNode(2)
    l4.right = l8
    l9 = TreeNode(5)
    l6.left = l9
    l10 = TreeNode(1)
    l6.right = l10

    sol = Solution()
    max = sol.pathSum(l1, 22)
    sol.print_list(max)
