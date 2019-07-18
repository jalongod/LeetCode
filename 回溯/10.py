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

    # 增加支持'*'
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        first_match = (not len(s) == 0) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            # 发现通配符
            return self.isMatch(s, p[2:]) or (first_match
                                              and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    sol = Solution()
    # max = sol.isMatch("aa", "a")  # false
    # max = sol.isMatch("aa", "a*")  #true
    max = sol.isMatch("ab", ".*")  #true
    # max = sol.isMatch("aab", "c*a*b")  #true
    # max = sol.isMatch("mississippi", "mis*is*p*.")  #false
    print(max)