def InsertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        k = arr[i]
        j = i - 1
        while j > -1:
            if arr[j] > k:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = k


a = [7, 2, 4, 1, 5, 3]
InsertionSort(a)
print(a)
