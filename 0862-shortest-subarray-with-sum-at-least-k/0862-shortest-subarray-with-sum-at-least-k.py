class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pre = [0]
        for num in A:
            pre.append(pre[-1]+num)
            
        deque = collections.deque()
        result = float(inf)
        for i,sum_ in enumerate(pre):
            
            while(deque and deque[-1][1] >=sum_):
                deque.pop()
            
            while deque and sum_ - deque[0][1] >= K:
                result = min(i-deque[0][0], result)
                deque.popleft()
                
            deque.append([i,sum_])
        return result if result!= float(inf) else -1
        