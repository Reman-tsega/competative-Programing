# strategy
# remove the most frequent element until the arr size becomes less than or seual to half of the array
# 1 get half of the array
# sort the array based on freq in desending order
# use the no as key to its freq and count both the iteration and sum of the count based on the condition half
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half_size = len(arr)//2
        count=0
        size_of_removed_num=0
        freq_data =Counter(arr).most_common()
        
        for key,value in freq_data:
            count+=1
            size_of_removed_num+=value
            if size_of_removed_num>=half_size:
                return count
