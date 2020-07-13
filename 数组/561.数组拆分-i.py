#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        res = 0
        if not nums or not len(nums):
            return res
        mresult = self.mergeSort(nums)
        for i in range(0,len(mresult),2):
            res+=mresult[i]
        return res
    def mergeSort(self,nums):
        if len(nums)<2:
            return nums
        lth = len(nums)
        return self.merge(self.mergeSort(nums[:lth//2]),self.mergeSort(nums[lth//2:]))
    
    def merge(self,arr1,arr2):
        res = []
        index1,index2 = 0,0
        while index1<len(arr1) and index2<len(arr2):
            if arr1[index1]<arr2[index2]:
                res.append(arr1[index1])
                index1+=1
            else:
                res.append(arr2[index2])
                index2+=1
        if index1<len(arr1):
            res.extend(arr1[index1:])
        elif index2<len(arr2):
            res.extend(arr2[index2:])
        return res
        
            
# @lc code=end

