class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
		
        leftSum, rightSum = 0, sum(nums)
        
        for i, v in enumerate(nums):
            rightSum -= v
            if leftSum == rightSum:
                return i
            leftSum += v
            
        return -1