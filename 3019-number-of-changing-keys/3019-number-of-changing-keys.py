class Solution:
    def countKeyChanges(self, s: str) -> int:
        # iterate over the string by using the two consecative index
        #and compare their value , if they are diferent there is a change

        # define variable to store count(0)
        # use for loop to iterate the string using index stating from 0 up to n-1
        # use if to compare the i and i+1 up to n-1

        count_change=0
        lowerCase_s= s.lower()
        for i in range(len(s)-1):
            if(lowerCase_s[i]!=lowerCase_s[i+1]):
                count_change+=1
        return count_change