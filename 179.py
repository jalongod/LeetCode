'''
179. 最大数
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:  # 基数排序
    def largestNumber(self, nums) -> str:
        sort_nums = self.merge_sort(nums)
        isZero = True
        for num in sort_nums:
            if num != 0:
                isZero = False
        if isZero:
            return "0"
        return "".join([str(_) for _ in sort_nums])

    def merge_sort(self, arr):
        def merge(arr1, arr2):
            res = []
            while len(arr1) and len(arr2):
                # print(str(arr1[0]) + str(arr2[0]))
                # print(str(arr2[0]) + str(arr1[0]))
                if str(arr1[0]) + str(arr2[0]) > str(arr2[0]) + str(arr1[0]):
                    res.append(arr1[0])
                    arr1.pop(0)
                else:
                    res.append(arr2[0])
                    arr2.pop(0)
            if len(arr1):
                res.extend(arr1)
            elif len(arr2):
                res.extend(arr2)
            return res

        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        return merge(self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:]))

    # 基数排序不能解决问题
    def radix_sort(self, arr):
        # res = []
        if len(arr) <= 0:
            return ""
        max_num = max(arr)
        max_num_len = len(str(max_num))
        i = max_num_len - 1  # 当前正在处理的位数值
        while i >= 0:
            bucket_list = [[] for _ in range(10)]
            for item in arr:
                wei = int(item / (10**i)) % 10
                bucket_list[wei].append(item)
            # print(bucket_list)
            arr.clear()
            for bucket in bucket_list:
                for v in bucket:
                    arr.insert(0, v)
            i -= 1
            pass
        return "".join([str(_) for _ in arr])


sol = Solution()
# len = sol.largestNumber([3, 30, 34, 5, 9])
# len = sol.largestNumber([20, 1])
# len = sol.largestNumber([])
len = sol.largestNumber([0, 0])
print(str(len))
