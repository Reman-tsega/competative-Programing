class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        most_freq = Counter(sorted(words)).most_common()
        # kth_freq_word = 
       
        return [most_freq[i][0] for i in range(k)]
        # num_dict = Counter(words) #provide key as num and freq as val
        # sort_fa = sorted(num_dict, key= lambda x:(-num_dict[x],x))
        # return sort_fa[:k]
        