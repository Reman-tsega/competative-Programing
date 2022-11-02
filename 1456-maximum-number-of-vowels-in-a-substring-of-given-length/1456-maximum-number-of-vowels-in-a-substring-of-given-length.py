class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = j = vowels = 0
        for i, c in enumerate(s):
            vowels += c in 'aeiou' 
            if i - j + 1 > k:
                vowels -= s[j] in 'aeiou'
                j += 1    
            if i - j + 1 == k:    
                res = max(res, vowels)
        return res 
        