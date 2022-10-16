class Solution:
    def validateStackSequences(self, pushed, popped):
        ind1, ind2, n = 0, 0, len(pushed)
        stack = []
        while ind1 < n or ind2 < n:
            if stack and stack[-1] == popped[ind2]:
                stack.pop()
                ind2 += 1
            elif ind1 < n:
                stack.append(pushed[ind1])
                ind1 += 1
            else:
                return False
        
        return True
        