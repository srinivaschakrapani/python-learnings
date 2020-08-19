def BinarySearch(a, x):
    if len(a) == 1:
        return a[0] == x
    mid = len(a) // 2
    if x > a[mid]:
        return BinarySearch(a[mid:], x)
    else:
        return BinarySearch(a[:mid], x)


arr = [i for i in range(1, 10)]
print(BinarySearch(arr, 9))