'''
6. Z 字形变换

'''


class Solution:
    def convert(self, string: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        i, rev = 0, False  # rev 是否是倒叙
        for s in string:
            res[i].append(s)
            # 如果正序，而且i==lens-1 rev=!rev
            # 如果倒序，而且i==0 rev=!rev
            if (not rev and i == numRows - 1) or (rev and i == 0):
                rev = not rev
            i = min(i + 1, numRows - 1) if not rev else max(i - 1, 0)

        return "".join(["".join(res[i]) for i in range(numRows)])


sol = Solution()
# max = sol.convert("LEETCODEISHIRING", 3)
# print(max)
max = sol.convert("ABC", 1)
print(max)
