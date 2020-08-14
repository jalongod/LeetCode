'''
164. 最大间距

给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
如果数组元素个数小于 2，则返回 0。


示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def maximumGap(self, nums) -> int:
        def merge_sort(arr):
            def merge(arr1, arr2):
                res = []
                while len(arr1) > 0 and len(arr2) > 0:
                    if arr1[0] > arr2[0]:
                        res.append(arr2[0])
                        arr2.pop(0)
                    else:
                        res.append(arr1[0])
                        arr1.pop(0)
                res.extend(arr1 if len(arr1) > 0 else arr2)
                return res

            if len(arr) < 2:
                return arr

            return merge(merge_sort(arr[:len(arr) // 2]),
                         merge_sort(arr[len(arr) // 2:]))

        sort_nums = merge_sort(nums)
        res = 0
        for i in range(len(sort_nums) - 1):
            res = max(res, sort_nums[i + 1] - sort_nums[i])
        return res


sol = Solution()
len = sol.maximumGap([3, 6, 10, 1])
print(str(len))
