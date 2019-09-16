'''
282. 给表达式添加运算符
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 
示例 2:

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
示例 3:

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
示例 4:

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]
示例 5:

输入: num = "3456237490", target = 9191
输出: []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/expression-add-operators
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def calculate(num, target, expression, prev, ans, results):
            if len(num) == 0 and ans == target:
                results.append(expression)
            else:
                for i in range(1, len(num) + 1):
                    if i > 1 and num[0] == '0':
                        continue
                    a = int(num[0:i])
                    if expression == '':
                        calculate(num[i:len(num)], target, num[0:i], a, a,
                                  results)
                    else:
                        calculate(num[i:len(num)], target,
                                  expression + '+' + num[0:i], a, ans + a,
                                  results)
                        calculate(num[i:len(num)], target,
                                  expression + '-' + num[0:i], -a, ans - a,
                                  results)
                        calculate(num[i:len(num)], target,
                                  expression + '*' + num[0:i], a * prev,
                                  ans + prev * (a - 1), results)

        results = []
        calculate(num, target, '', 0, 0, results)
        return results


sol = Solution()
len = sol.addOperators("105", 5)
print(str(len))
