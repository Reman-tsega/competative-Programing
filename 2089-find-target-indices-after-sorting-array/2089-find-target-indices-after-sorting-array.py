class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_index=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                target_index.append(i)
        return target_index
        