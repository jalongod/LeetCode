'''
89. 格雷编码
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。

给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。

00 - 0
10 - 2
11 - 3
01 - 1
示例 2:

输入: 0
输出: [0]
解释: 我们定义格雷编码序列必须以 0 开头。
     给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
     因此，当 n = 0 时，其格雷编码序列为 [0]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # 递归
    # 公式 grayCode(i) = ['0'+node for node in grayCode[i-1]]正序 +['1'+node for node in grayCode[i-1] 逆序]
    # grayCode(0)=[0]  grayCode(1)=['0','1']
    def grayCode(self, n: int):
        def recur(n):
            if n == 0:
                return ['0']
            if n == 1:
                return ['0', '1']
            pre = recur(n - 1)
            cur = []
            for index in range(0, len(pre)):
                cur.append('0' + pre[index])
            for index in range(len(pre) - 1, -1, -1):
                cur.append('1' + pre[index])
            return cur

        res = []
        cur = recur(n)
        for node in cur:
            res.append(int(node, 2))
        return res

    # 动态规划
    # 公式 dp(i) = ['0'+node for node in grayCode[i-1]]正序 +['1'+node for node in grayCode[i-1] 逆序]
    # grayCode(0)=[0]  grayCode(1)=['0','1']
    # 最后转为
    def grayCode2(self, n: int):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0', '1']
        pre = ['0', '1']
        for index in range(n - 1):
            cur = []
            for index in range(0, len(pre)):
                cur.append('0' + pre[index])
            for index in range(len(pre) - 1, -1, -1):
                cur.append('1' + pre[index])
            pre = cur
        res = []
        for node in cur:
            res.append(int(node, 2))
        return res


sol = Solution()
r1 = sol.grayCode(3)
r2 = sol.grayCode2(3)
print('=======' + max)
