arr= [2,1,7,3,6,5]
n= len(arr)
def insertionSort(arr, n):
  for i in range(1,n):
      for j in range(i,0,-1):
          if arr[j-1]>arr[j]:
              arr[j],arr[j-1]=arr[j-1],arr[j]
          else:
              break
  return arr
