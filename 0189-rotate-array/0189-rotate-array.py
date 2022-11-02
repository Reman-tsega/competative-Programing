class Solution:
    def rotate(self, nums, k):
   
        k = k % len(nums)
        count = 0
        start = 0
        while count<len(nums):
            prev = nums[start]
            current = start
            while True:
                next = (k+current)%len(nums)
                prev,nums[next]=nums[next], prev
                count+=1
                current = next
                if start==current:
                    break
            start+=1
                    
