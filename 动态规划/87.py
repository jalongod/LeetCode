'''
87. 扰乱字符串

'''
'''
动态规划求解（备忘录法）
循环将字符串s1, s2分割成长度（设长度为i）一样的子串（设为s11, s12, s21, s22），如果分割之后的子串是扰乱字符串，则分割前的字符串
也为扰乱字符串。
对于s2有两种分割方式：从i位置分和从s2.length - i位置分。

'''


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = dict()

        def dfs(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            l1, l2 = len(s1), len(s2)
            if l1 != l2:
                memo[(s1, s2)] = False
                return False
            if l1 < 4:
                memo[(s1, s2)] = sorted(s1) == sorted(s2)
                return memo[(s1, s2)]
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            if sorted(s1) != sorted(s2):
                return False
            memo[(s1, s2)] = False
            for k in range(1, l1):
                a = s1[:k]
                b = s2[:k]
                c = s1[k:]
                d = s2[k:]
                e = s2[l1 - k:]
                f = s2[:l1 - k]
                if (dfs(a, b) and dfs(c, d)) or (dfs(a, e) and dfs(c, f)):
                    memo[(s1, s2)] = True
                    return memo[(s1, s2)]
            return memo[(s1, s2)]

        return dfs(s1, s2)


class Solution2:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = dict()

        def dfs(s1: str, s2: str) -> bool:
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            l1, l2 = len(s1), len(s2)
            if l1 != l2:
                memo[(s1, s2)] = False
                return memo[(s1, s2)]
            leng = len(s1)
            if l1 < 4:
                memo[(s1, s2)] = sorted(s1) == sorted(s2)
                return memo[(s1, s2)]
            if s1 == s2:  # 重要
                memo[(s1, s2)] = True
                return True
            if sorted(s1) != sorted(s2):  # 重要
                return False
            res = False
            for k in range(1, leng):
                a = s1[:k]
                b = s2[:k]
                c = s1[k:]
                d = s2[k:]
                e = s2[leng - k:]
                f = s2[:leng - k]
                if (dfs(a, b) and dfs(c, d)) or (dfs(a, e) and dfs(c, f)):
                    memo[(s1, s2)] = True
                    return memo[(s1, s2)]

            return res

        return dfs(s1, s2)


sol = Solution()
# res = sol.isScramble("great", "rgeat")
# print(str(res))
# res = sol.isScramble("abcde", "caebd")
# print(str(res))
# res = sol.isScramble("abb", "bab")
# print(str(res))
# res = sol.isScramble("abcdefghijklmn", "efghijklmncadb")
# print(str(res))

sol2 = Solution2()
res2 = sol2.isScramble("abcdefghijklmn", "efghijklmncadb")
print(str(res2))
