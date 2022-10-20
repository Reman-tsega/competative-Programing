class Solution(object):
    def lengthOfLongestSubstring(self, s):
        subs=''
        max_len=0
        i=0
        while(i<len(s)):
            if s[i] not in subs:
                subs+=s[i]
            else:
                subs=subs[subs.index(s[i])+1:]+s[i]
            max_len= max(len(subs),max_len)
            i+=1
        return max_len;
                
        
 #Empty Sub String for saving Char
# max length substring
# Starting point
# Add char is not in sub string
# Take substring from last found index of char + 1
# Max length of substring