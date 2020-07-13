'''
84. 柱状图中最大的矩形

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例:

输入: [2,1,5,6,2,3]
输出: 10
'''
'''
暴力法 分析：
    求最大的面积，面积等于width*height，最终结果是找到某个i使得width(i)*heights[i]是最大的
    可以先求area[i]，随着数组增加每个i,所有的area[i]都要重新计算
    heights[i]是固定的，需要求width[i]

i:[0:]
j:[0:i]
max_array[j] 以h[j]为高度的最大面积
'''


class Solution:
    def largestRectangleArea(self, h) -> int:
        length = len(h)
        widths = [1 for _ in range(length)]
        max_area = 0
        for i in range(length):  # 求i的最大宽度
            for j in range(i - 1, -1, -1):
                if h[j] >= h[i]:
                    widths[i] += 1
                else:
                    break
            for k in range(i + 1, length):
                if h[k] >= h[i]:
                    widths[i] += 1
                else:
                    break
            max_area = max(widths[i] * h[i], max_area)
        return max_area


'''
第二种暴力解决办法
minheight=min(minheight,heights(j))
'''


class Solution2:
    def largestRectangleArea(self, h) -> int:
        max_area = 0
        length = len(h)
        for i in range(length):
            min_height = float("inf")
            for j in range(i, length):
                min_height = min(min_height, h[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


'''
分治
'''


class Solution3:
    def largestRectangleArea(self, h) -> int:
        if len(h) == 0:
            return 0
        min_index = h.index(min(h))
        leftLarge = self.largestRectangleArea(h[:min_index])
        midLarge = h[min_index] * len(h)
        rightLarge = self.largestRectangleArea(h[min_index + 1:])
        return max(leftLarge, midLarge, rightLarge)


sol = Solution3()
# res = sol.largestRectangleArea([2, 1, 5, 6, 2, 3])
res = sol.largestRectangleArea([3, 1, 3, 2, 2])
print(str(res))
