'''
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # dp
    # dp 定义以i为结尾的子串的子集
    # dp公式 dp[i] = dp[i-1]+ [node+nums[i] for node in dp[i-1]]  剪枝：if node+nums[i] in pre ; return

    def subsetsWithDup(self, nums):
        pre = [[]]
        for i in range(len(nums)):
            cur = []
            for node in pre:
                nnode = node + [nums[i]]
                nnode.sort()
                if nnode not in pre:
                    cur.append(nnode)
            # pre.append(cur[:])
            for n in cur:
                pre.append(n)
        return pre


sol = Solution()
max = sol.subsetsWithDup([4, 4, 4, 1, 4])
# max = sol.subsets2([1, 2, 3])
# max = sol.subsets3([1, 2, 3])
print(max)