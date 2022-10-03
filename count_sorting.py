def countingSort(arr):
    # Write your code here
    # create count list with 0 value and ==len(arr)
    # by using arr element as and index increment the count elements by 1 for each element of arr
    # change the count to index + 1 list
    # create new list b and put elements sortingly based on the count index

    count = [0]*100
    n=len(arr)
    for i in range(n):
        count[arr[i]]+=1
    for j in range(1,n):
        count[j]=count[j]+count[j-1]
    b=[0]*100
    for k in range(n-1,0,-1):
        b[count[arr[k]]-1]= arr[k]
        count[arr[k]]-=1
        
    for m in range(n):
        arr[m]=b[m]
    return arr
