'''
反转字符串
如 ABCD
返回 DCBA
'''


def reverse1(str):  # 非递归 栈
    if not str or len(str) == 1:
        return str
    stack = []
    for i in range(len(str)):
        stack.append(str[i])
    res = ""
    while len(stack):
        res += stack[len(stack) - 1]
        stack.pop()
    return res


def reverse2(str):  # 递归
    if not str or len(str) <= 1:
        return str
    res = reverse2(str[1:]) + str[:1]
    return res
    pass


res = reverse1("ABCD")
print(res)
res = reverse2("ABCD")
print(res)
