class Solution:
    def rotate(self, nums, k):
   
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1
        