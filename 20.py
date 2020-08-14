'''
20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in dic:
                if len(stack) == 0 or stack[len(stack) - 1] != dic.get(c):
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0


sol = Solution()
max = sol.isValid("[]")
print(max)
