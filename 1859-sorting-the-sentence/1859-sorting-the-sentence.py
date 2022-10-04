class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        words.sort(key= lambda l:int(l[-1]))
        removed_word= map(lambda word:word.replace(word[-1],''),words)
        sentence = " ".join(removed_word)
        return sentence
        