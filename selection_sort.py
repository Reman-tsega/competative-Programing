class Solution:
    def selectionSort(self, arr,n):
        #code here
        t=0
        for i in range(n):
            index_of_min=i
            for s in range(t,n):#0 1 2 3
                if arr[index_of_min] > arr[s]: 
                   # min=arr[s] #1 3 7
                    index_of_min=s#1 2 4
            
            arr[i],arr[index_of_min] = arr[index_of_min],arr[i]
            t+=1
                
        return arr
