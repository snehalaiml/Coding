def removedup(arr):
    k = 0
    for i in range(1,len(arr)):
        if arr[k] != arr[i]:
            k+=1
            arr[k] = arr[i]
    return arr

arr = [1,1,2,3,4,4]
print(removedup(arr))