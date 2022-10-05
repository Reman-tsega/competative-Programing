class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        parentheses ={
            '(':')',
            '[':']',
            '{':'}'
        }
        
        for i in s:
            if i in parentheses:
                stack.append(parentheses[i])
            elif len(stack)==0 or stack.pop()!= i :
                return False
        return not len(stack)