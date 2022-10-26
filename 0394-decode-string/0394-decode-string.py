class Solution:
    def decodeString(self, s: str) -> str:
        curs=''
        curn='0'
        stack =[]
        # temp=''
        for i in s:
            if i.isnumeric():
                curn = curn + i
            elif i=='[':
                stack.append((curs,curn))
                curs=''
                curn='0'
            elif i==']':
                prevs, prevn = stack.pop()
                curs = prevs + (curs*int(prevn))
            else:
                curs+=i
        return curs
        
        
        
        
