'''
3. 无重复字符的最长子串

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
动态规划
dp[i] 以i为底的最长子序列
dp[0] = s[0]
1.如果s[i]不在dp[i-1]中 dp[i] = dp[i-1]+s[i]
2.如果s[i]在dp[i-1]中 dp[i] = s[i]
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [[] for n in range(n)]
        dp[0].append(s[0])
        max_array = []
        for i in range(1, n):
            if dp[i - 1].__contains__(s[i]):
                index = dp[i - 1].index(s[i])
                if not index == len(dp[i - 1]) - 1:
                    dp[i].extend(dp[i - 1][index + 1:])
            else:
                dp[i].extend(dp[i - 1])
            dp[i].append(s[i])
            if len(dp[i]) > len(max_array):
                max_array = dp[i]
        return len(max_array)


sol = Solution()
max = sol.lengthOfLongestSubstring("dvdf")
print(max)
