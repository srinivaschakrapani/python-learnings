def sort012(arr, n):
    # Your code goes here
    l = [None] * n
    nz = 0
    n2 = n - 1
    for i in arr:
        if i == 0:
            l[nz] = 0
            nz += 1
        elif i == 2:
            l[n2] = 2
            n2 -= 1
    for k in range(nz, n2+1):
        l[k] = 1
    for k in range(n):
        arr[k] = l[k]
    print(arr)

arr = [0,1,2,0,2,0,1]
n = len(arr)
sort012(arr,n)