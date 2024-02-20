class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # probles
        # givent that there is list of num [0,n]
        # find the missing number 

        # soln
        # sprt the list
        # iternate upto len(num)
        # return the index if the num[i] and i not equal
        # if it is equal for all index's return i+1

        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1

        