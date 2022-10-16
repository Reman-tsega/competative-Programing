class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                left = stack.pop()
                answer[left] = i - left # day difference
            stack.append(i)
        return answer