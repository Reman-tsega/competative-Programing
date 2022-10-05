class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        lbi=0
        ubi=len(nums)-1 #3
        
        while(lbi<=ubi):
            mid= lbi+(ubi-lbi)//2 #0
            
            # if target not in nums:
            #     return -1
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lbi= mid+1#1
            elif nums[mid]> target:
                ubi= mid-1 #0
        return -1
