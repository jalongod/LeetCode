'''
56. 合并区间

给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def merge(self, intervals):
        sort_intervals = self.quit_sort(intervals)
        res = []

        for item in sort_intervals:
            if len(res) <= 0:
                res.append(sort_intervals[0])
                continue
            tail = res[len(res) - 1]
            if item[0] <= tail[1]:
                tail[1] = max(tail[1], item[1])
            else:
                res.append(item)
        return res

    def quit_sort(self, intervals):
        if len(intervals) < 2:
            return intervals
        left, right = [], []
        mid = intervals[len(intervals) // 2]
        intervals.pop(len(intervals) // 2)
        for item in intervals:
            if item[0] == mid[0]:
                mid[1] = max(item[1], mid[1])
            elif item[0] > mid[0]:
                right.append(item)
            else:
                left.append(item)

        return self.quit_sort(left) + [mid] + self.quit_sort(right)


sol = Solution()
len = sol.merge([[8, 10], [1, 3], [2, 6], [1, 4], [1, 6], [15, 18]])
print(str(len))
