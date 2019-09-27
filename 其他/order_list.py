'''
某电商平台有n类商品
订单格式为[i,j,k],表示预定从商品i到j，每一类预定k个
请返回长度为n的数组表示所有订单量
比如：
orderlist = [[2,4,10],[0,3,15],[3,4,21]] n =6
返回[15,15,25,46,31,0]
'''


class Solution:
    def all_order(self, order_list, n: int):
        if n <= 0:
            return 0
        res = [0] * n
        for order in order_list:
            left, right, value = order[0], order[1], order[2]
            for i in range(left, right + 1):
                res[i] += value
        return res


sol = Solution()
len = sol.all_order([[2, 4, 10], [0, 3, 15], [3, 4, 21]], 6)
print(str(len))
