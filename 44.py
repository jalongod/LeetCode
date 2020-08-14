'''
44.通配符匹配

给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:

    # 常规匹配算法
    # def isMatch(self, s: str, p: str) -> bool:
    #     if len(p) == 0:
    #         return len(s) == 0
    #     first_match = (not len(s) == 0) and p[0] == s[0]
    #     return first_match and self.isMatch(s[1:], p[1:])

    # 增加支持 '.'
    # def isMatch(self, s: str, p: str) -> bool:
    #     if len(p) == 0:
    #         return len(s) == 0
    #     first_match = (not len(s) == 0) and p[0] in {s[0], '.'}
    #     return first_match and self.isMatch(s[1:], p[1:])

    # 增加支持'*' '*' 匹配零个或多个前面的那一个元素
    # def isMatch(self, s: str, p: str) -> bool:
    #     if len(p) == 0:
    #         return len(s) == 0
    #     first_match = (not len(s) == 0) and p[0] in {s[0], '.'}
    #     if len(p) >= 2 and p[1] == '*':
    #         # 发现通配符
    #         return self.isMatch(s, p[2:]) or (first_match
    #                                           and self.isMatch(s[1:], p))
    #     else:
    #         return first_match and self.isMatch(s[1:], p[1:])

    # 增加支持'*'   '*' 可以匹配任意字符串（包括空字符串）。
    # 超过时间限制，回溯算法
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        first_match = (not len(s) == 0) and p[0] in {s[0], '?'}
        if first_match:
            return self.isMatch(s[1:], p[1:])
        first_match_all = p[0] in {'*'}
        if first_match_all:
            for i in range(len(s) + 1):
                if self.isMatch(s[i:], p[1:]):
                    return True
            return False
        return False


class Solution2:
    # dp[i][j]表示s到i位置,p到j位置是否匹配!
    # 动态规划
    def isMatch(self, s, p):
        sn = len(s)
        pn = len(p)
        if sn == pn == 0:
            return True
        if pn == 0:
            return False
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        # if (p[0] == '*'):
        #     dp[0][1] = True
        for j in range(1, pn + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution2()
    max = sol.isMatch("aa", "a")  # false
    print(max)
    max = sol.isMatch("aa", "a*")  #true
    print(max)
    max = sol.isMatch("aab", "c*a*b")  # false
    print(max)
    max = sol.isMatch("aab", "c*a*b")  #true
    print(max)
    max = sol.isMatch("mississippi", "mis*is*p*.")  #false
    print(max)
    max = sol.isMatch("", "*")  # false
    print(max)

    max = sol.isMatch("bbbaaabbababbaabbabbbbba", "*ab*****b")  # false
    print(max)