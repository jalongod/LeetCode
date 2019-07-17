'''
# 最长回文字符串

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        a = list(s)
        dp = [[False]*n for i in range(n)]
        res = a[0]
        max_len = 1
        for r in range(1, n):
            for l in range(r):
                if a[l] == a[r] and (l+1 <= r-1 or dp[l+1][r-1]):
                    dp[l][r] = True
                    cur_len = r-l+1
                    if cur_len > max_len:
                        max_len = cur_len
                        res = a[l:r+1]
        return res
                


if __name__ == '__main__':

    sol = Solution()
    max = sol.longestPalindrome("babad")
    print(max)