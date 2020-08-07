def arrayRotateCheck(arr, n):
    #Your code goes here
    r = 0
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            continue
        elif arr[i] < arr[i+1]:
            r = i + 1
    return r

arr = [6,7,8,1,2,3,4,5]
n = 5
print(arrayRotateCheck(arr,n))