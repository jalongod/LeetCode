'''
32. 最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
我们用 dp[i] 表示以 i 结尾的最长有效括号的长度；
1.当s[i]=='('，那么dp[i]=0
2.当s[i]==')'
    如果s[i-1]=='('，那么dp[i]=dp[i-2]+2
    如果s[i-1]==')' 并且s[i-dp[i-1]-1]=='('
        那么dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2]
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[
                        i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        return max(dp)


# 获取合法括号对数量
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        for c in s:
            # print(str(len(stack)))
            if len(stack) != 0 and stack[len(stack) - 1] == '(' and c == ')':
                max_len += 1
                stack.pop()
            else:
                stack.append(c)

        return max_len


sol = Solution()
len = sol.longestValidParentheses(")()())")
print(str(len))