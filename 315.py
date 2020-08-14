'''
315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  
nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0] 
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # 节点值
        self.count = 0  # 左子树节点数量  右侧小于该数字的个数


class Solution:  # BST解法 倒叙插入就可以
    def countSmaller(self, nums):
        length = len(nums)
        root = None

        res = [0 for _ in range(length)]
        for i in reversed(range(length)):
            root = self.insertNode(root, nums[i], res, i)
        return res

    # 插入BST 将val插入到以root为根的BST中，返回根节点
    def insertNode(self, root, val, res, res_index):
        if root is None:
            root = TreeNode(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, val, res, res_index)
        elif val > root.val:
            res[res_index] += root.count + 1
            root.right = self.insertNode(root.right, val, res, res_index)
        return root


sol = Solution()
# len = sol.hIndex([3, 0, 6, 1, 5])
len = sol.countSmaller([5, 2, 6, 1])

print(str(len))
