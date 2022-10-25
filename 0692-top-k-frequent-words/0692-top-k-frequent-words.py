class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        most_freq = Counter(sorted(words)).most_common()
        # kth_freq_word = 
       
        return [most_freq[i][0] for i in range(k)]
        