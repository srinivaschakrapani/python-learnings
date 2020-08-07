from sys import stdin


def secondLargestElement(arr, n):
    # Your code goes here
    min_int = -2147483648
    if n <= 1 or arr.count(arr[0]) == n:
        return min_int
    fmax = arr[0]
    smax = arr[1]

    if fmax < smax:
        fmax, smax = smax, fmax

    if fmax == smax:
        smax = min_int

    for i in range(2, n):
        if arr[i] > fmax:
            smax = fmax
            fmax = arr[i]
        elif arr[i] > smax and arr[i] != fmax:
            smax = arr[i]
    return smax


arr = [90, 8, 90,5]
n = len(arr)
print('Fucntion call')
print(secondLargestElement(arr, n))
