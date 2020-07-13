'''
确定指定数组中逆序对的个数
'''


class Solution:
    res_count = 0

    def rev_order_count(self, order_list):
        if not order_list or len(order_list) < 2:
            return order_list

        def merge2(l1, l2):
            res = []
            index1, index2 = 0, 0
            while (index1 < len(l1) and index2 < len(l2)):
                if l1[index1] <= l2[index2]:
                    res.append(l1[index1])
                    index1 += 1
                else:
                    self.res_count += index2 + 1  # res ++  # 关键是这里
                    res.append(l2[index2])
                    index2 += 1
            if index1 < len(l1):
                # res.extend(arr1[index1:])
                while (index1 < len(l1)):  # 附加l1
                    # self.res_count += index2
                    res.append(l1[index1])
                    index1 += 1
            elif index2 < len(l2):
                # res.extend(arr2[index2:])
                while (index2 < len(l2)):
                    res.append(l2[index2])
                    index2 += 1
            return res

        return merge2(self.rev_order_count(order_list[:len(order_list) // 2]),
                      self.rev_order_count(order_list[len(order_list) // 2:]))


sol = Solution()
len = sol.rev_order_count([7, 6, 5, 4])
print(str(sol.res_count))
