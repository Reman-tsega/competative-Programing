class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        lbi=0
        ubi=len(nums)-1 
        
        while(lbi<=ubi):
            mid= lbi+(ubi-lbi)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                lbi= mid+1
            elif nums[mid]> target:
                ubi= mid-1 
        return -1
