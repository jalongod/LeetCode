'''
312. 戳气球
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167 
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    # 回溯、超时了，应该找一下剪枝策略
    def maxCoins(self, nums: List[int]) -> int:
        max_val = 0

        def breakfun(nums, val):
            nonlocal max_val
            if len(nums) == 2:
                max_val = max(max_val, val)
            for i in range(1, len(nums) - 1):
                pre, cur, tail, obj = nums[i -
                                           1], nums[i], nums[i +
                                                             1], nums.pop(i)
                breakfun(nums, pre * tail * cur + val)
                nums.insert(i, obj)

        nums.insert(0, 1)
        nums.append(1)
        breakfun(nums, 0)
        return max_val


class Solution2:
    # dp[i][j] 表示戳破[i+1 ... j-1]号气球的最大收益
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        # dp初始化
        for i in range(1, len(nums) - 1):
            dp[i][i] = nums[i - 1] * nums[i] * nums[i + 1]
        for i in range(1, len(nums) - 1):
            pass


sol = Solution()
# len = sol.maxCoins([3, 1, 5, 8])
len = sol.maxCoins([])
print(str(len))
