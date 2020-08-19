def BubbleSort(arr):
    end = len(arr)
    i = 0
    n = end
    swaps = 1
    while i < end and swaps > 0:
        swaps = 0
        for k in range(0, n - 1):

            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                swaps += 1
        n -= 1
        i += 1
        print("Intermediate Sort-->", arr)


arr = [10, 8, 9, 4, 6, 1, 3, 2]
BubbleSort(arr)
print(arr)
