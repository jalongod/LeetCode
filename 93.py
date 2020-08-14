'''
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or s == "":
            return []

        def getIp(s, length, begin, path):
            nonlocal res
            if (4 - len(path)) * 3 < length - begin:
                return
            if len(path) == 4:
                res.append(".".join(path))
            else:
                for l in range(1, 4):
                    if begin + l > length:
                        break
                    st = s[begin:begin + l]
                    if len(st) > 1 and st[0] == '0':
                        continue
                    val = int(st)
                    if val > 255:
                        continue
                    path.append(s[begin:begin + l])
                    begin += l
                    getIp(s, length, begin, path)
                    path.pop()
                    begin -= l
            pass

        res = []
        getIp(s, len(s), 0, [])
        return res


if __name__ == '__main__':
    sol = Solution()
    # max = sol.restoreIpAddresses("25525511135")
    max = sol.restoreIpAddresses("010010")

    print(max)
