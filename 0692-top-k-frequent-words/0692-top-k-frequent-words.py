class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        most_freq = Counter(sorted(words)).most_common()
        kth_freq_word = []
        for i in range(k):
            kth_freq_word.append(most_freq[i][0])
        return kth_freq_word
        