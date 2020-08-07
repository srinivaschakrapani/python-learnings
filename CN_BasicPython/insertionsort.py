def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        k = arr[i]
        while k < arr[j - 1] and j > 0:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = k
    print(arr)


insertionsort([6, 5, 3, 9, 0])
