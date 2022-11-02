class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        count = 0
        sum_ = 0
        map_ = {
            0: 1
        }
        for i in range(len(n)):
            sum_+=n[i]
            if sum_ - k in map_:
                count+=map_[sum_ - k]
            if sum_ in map_:
                map_[sum_]+=1
            else:
                map_[sum_]=1
        return count