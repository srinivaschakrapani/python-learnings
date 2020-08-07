def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minindex = i
        replaceindex = i
        for j in range(i + 1, n):
            if arr[minindex] >= arr[j]:
                replaceindex = j
        if minindex != replaceindex:
            arr[minindex], arr[replaceindex] = arr[replaceindex], arr[minindex]
    for i in arr:
        print(i, end=" ")


#arr = [11, 25, 12, 22, 64]
arr = [1, 3, 2, 4, 0, 6, 8]
print(arr)
selectionsort(arr)
