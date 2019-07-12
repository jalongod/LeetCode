# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        # 取nums列表的中间下标值
        mid_index = len(nums)//2
        pNode = TreeNode(nums[mid_index])
        pNode.left = self.sortedArrayToBST(nums[:mid_index])
        pNode.right = self.sortedArrayToBST(nums[mid_index+1:])
        return pNode


if __name__ == '__main__':
    sol = Solution()
    max = sol.sortedArrayToBST([0,1,2,3,4,5,6,7,8,9])
    print(max)