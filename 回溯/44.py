'''
正则表达式匹配
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