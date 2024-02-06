        # separate the words in a list
        # reverse the list
        # remove the space from list
        # rejoin th list with space

class Solution:
    def reverseWords(self, s: str) -> str:
        newlist = s.split(" ")
        print(newlist)
        return " ".join( [ i for i in newlist if len(i)> 0][::-1]).strip()

        