import math
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter=[0]*len(nums)
        i=0
        while(i<len(nums)):
            for j in range(len(nums)):
                if nums[i]> nums[j]:
                    counter[i]+=1
            i+=1
        return counter
        
