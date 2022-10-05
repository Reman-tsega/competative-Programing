class Solution:
    def reverseParentheses(self, s: str) -> str:
        sub =" "
        stack =[]
        
        for i in s:
            if i =='(':
                stack.append(sub)
                sub=""
            elif i==')':
                sub=stack.pop() + sub[::-1]
            else:
                sub+=i
        return sub.strip()
                
        
        