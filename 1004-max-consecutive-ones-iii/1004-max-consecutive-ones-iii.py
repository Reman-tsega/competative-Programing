class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        for j in range(len(nums)):
            if nums[j] == 0: 
                k -= 1
            if k < 0:
                if nums[l] == 0: 
                    k += 1
                l += 1
                
        return (j - l) + 1
        