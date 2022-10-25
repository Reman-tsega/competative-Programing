class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = Counter(nums).most_common()
        kth_num=[]
        for i in range(k) :
            kth_num.append(most_frequent[i][0])
        return kth_num;