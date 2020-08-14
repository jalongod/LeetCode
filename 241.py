'''
241. 为运算表达式设计优先级
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2
示例 2:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def helper(self, m, n, p):
        if p == "+":
            return m + n
        elif p == "-":
            return m - n
        else:
            return m * n

    def diffWaysToCompute(self, input: str) -> List[int]:
        # 递归终止条件
        if input.isdigit():
            return [int(input)]

        res = []
        for i, p in enumerate(input):
            if p in {'+', '-', '*'}:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        res.append(self.helper(l, r, p))
        return res


sol = Solution()
len = sol.diffWaysToCompute("2*3-4*5")
print(str(len))
