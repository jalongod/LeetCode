'''
22.括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def generateParenthesis(self, n: int):
        if n <= 0:
            return n
        res = []

        def gen(left, right, path):
            if left == n and right == n:
                res.append(path)
                return
            if left < n:
                gen(left + 1, right, path + '(')
            if right < n and right < left:
                gen(left, right + 1, path + ')')

        gen(0, 0, '')
        return res


if __name__ == '__main__':
    sol = Solution()
    max = sol.generateParenthesis(3)
    print(max)