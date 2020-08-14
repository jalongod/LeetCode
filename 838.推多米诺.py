#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#


# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if not dominoes or not len(dominoes):
            return dominoes
        dom = list(dominoes)
        dom.insert(0, 'L')
        dom.append('R')
        tags = []
        for i in range(len(dom)):
            if not dom[i] == '.':
                tags.append(i)

        def format(s, e):
            start = dom[s]
            end = dom[e]
            if start == "L" and end == "R":
                return
            if start == "L" and end == "L":
                for i in range(s, e):
                    dom[i] = 'L'
            if start == "R" and end == "R":
                for i in range(s, e):
                    dom[i] = 'R'
            if start == "R" and end == "L":
                jishu = True if (e - s) % 2 == 0 else False
                # 5  678 9 基数
                if jishu:
                    mid = s + (e - s) // 2
                    for i in range(s, mid):
                        dom[i] = 'R'
                    right = mid + 1
                    for i in range(right, e):
                        dom[i] = 'L'
                else:  # 5 6789 10 偶数
                    mid = s + (e - s) // 2
                    for i in range(s, mid + 1):
                        dom[i] = 'R'
                    for i in range(mid + 1, e):
                        dom[i] = 'L'

        for i in range(len(tags) - 1):
            start = tags[i]
            end = tags[i + 1]
            format(start, end)
        dom.pop(0)
        dom.pop()
        return ''.join(dom)


# @lc code=end

sol = Solution()
res = sol.pushDominoes(".L.R...LR..L..")
print(res)