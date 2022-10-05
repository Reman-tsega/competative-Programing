class Solution:
    
    # def divides(first_num,last_num):
    #     return (first_num // lasst_num)
    def sub(first_num,last_num):
        return first_num - lasst_num
    def mul (first_num, last_num):
        return first_num*last_num
    
    def add(first_num, last_num):
        return first_num+last_num
    
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        opration=['+','-','*','/']
        stack =[]
            
        for n in tokens:
            if n.isnumeric():
                stack.append(n)
            elif n in opration:
                last_num = int(stack.pop() )
                first_num = int(stack.pop() )
                
                if n=="+":
                    result = add(first_num,last_num)
                    stack.append(result)
                
                elif n=="*":
                    result = mul(first_num,last_num)
                    stack.append(result)
                elif n=="/":
                    result = int(first_num/last_num)
                    stack.append(result)
                elif n=="-":
                    result = sub(first_num,last_num)
                    stack.append(result)
            else:
                stack.append(n) # for negative number
                    
                
        return stack[0]
            
                
                
                