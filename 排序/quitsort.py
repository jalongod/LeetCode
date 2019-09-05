class Solution:
    def sort(self, intervals):
        # print(self.quick_sort(intervals))
        # print(self.bubble_sort(intervals))
        # print(self.select_sort(intervals))
        # print(self.insert_sort(intervals))
        # print(self.merge_sort(intervals))
        print(self.radix_sort(intervals))
        pass

    # 冒泡排序 O(N2)
    def bubble_sort(self, arr):
        if len(arr) < 2:
            return arr
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):  # 重要  len(arr)-i-1
                if arr[j] > arr[j + 1]:  # 重要 j  j+1
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # 选择排序 O(N2) 从待选列表中选择一个最小的放在待选列表前
    def select_sort(self, arr):
        if len(arr) < 2:
            return arr
        for i in range(len(arr)):
            min_index = i
            for j in range(i, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr

    # 插入排序 维护一段有序数列，同时遍历待排序的数列，在有序数列里找到合适的位置，插入元素。
    def insert_sort(self, arr):
        if len(arr) < 2:
            return arr
        for i in range(1, len(arr)):
            for j in range(i - 1, -1, -1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
        return arr

    # 归并排序 O(n log n)
    def merge_sort(self, arr):
        def merge_arr(arr1, arr2):
            res = []
            index1, index2 = 0, 0
            while index1 < len(arr1) and index2 < len(arr2):
                if arr1[index1] > arr2[index2]:
                    res.append(arr2[index2])
                    index2 += 1
                else:
                    res.append(arr1[index1])
                    index1 += 1
            if index1 < len(arr1):
                res.extend(arr1[index1:])
            elif index2 < len(arr2):
                res.extend(arr2[index2:])
            return res

        if len(arr) < 2:
            return arr
        len_arr = len(arr)
        return merge_arr(
            self.merge_sort(arr[:len_arr // 2]),
            self.merge_sort(arr[len_arr // 2:]),
        )

        pass

    # 快速排序 递归分治 时间复杂度 O(NlogN)
    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr
        mid = arr[len(arr) // 2]
        left, right = [], []
        arr.remove(mid)
        for item in arr:  # 重要
            if item < mid:
                left.append(item)
            else:
                right.append(item)
        return self.quick_sort(left) + [mid] + self.quick_sort(right)  # 重要

    # 桶排序
    def radix_sort(self, arr):
        # res = []
        i = 0  # 当前正在处理的位数值
        max_num = max(arr)
        max_num_len = len(str(max_num))
        while i < max_num_len:
            bucket_list = [[] for _ in range(10)]
            for item in arr:
                wei = int(item / (10**i)) % 10
                bucket_list[wei].append(item)
            # print(bucket_list)
            arr.clear()
            for bucket in bucket_list:
                for v in bucket:
                    arr.append(v)
            i += 1
            pass
        return arr

    # 希尔排序
    # 基数排序
    # 堆排序

    # 计数排序
    # 顾名思义统计待排序数列中每个数字出现的次数。填入数据结构的过程其实就是排序的过程。最后再按照统计结果覆盖原序列就行了。
    # 不是基于比较的排序，但是前提条件是知道排序元素的范围。


sol = Solution()
len = sol.sort([4, 2, 56, 2, 5, 6, 1, 49])
# print(str(len))
