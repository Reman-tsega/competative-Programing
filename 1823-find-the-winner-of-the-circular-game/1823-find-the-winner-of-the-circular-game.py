class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        k = k-1
        index = 0
        li = [i for i in range(1,n+1)]
        def cal(k,index):
            if len(li) == 1:
                return li[0]
            index = (index + k)% len(li)
            del li[index]
            return cal(k,index)
        return cal(k,index)
        