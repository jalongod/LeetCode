'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp[i] 以第i个数字为底的最大子序和
1.dp[0]= nums[0]
2.如果nums[i]<0 
    如果dp[i-1]>=0  dp[i] = dp[i-1]+nums[i]
    如果dp[i-1]<0 dp[i] = nums[i]
  如果nums[i]>0
    如果dp[i-1]<0 dp[i] = nums[i]
    如果dp[i-1]>=0 dp[i] = dp[i-1]+nums[i]
    故：
        如果dp[i-1]>=0 dp[i] = dp[i-1]+nums[i]
        如果dp[i-1]<0 dp[i] = nums[i]
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
        -3, 4, -1, 2
'''


class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)


sol = Solution()
max = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(str(max))
