arr = [1, 0, 1, 1, 0, 1, 0, 1]
n = 8
#arr = [0, 1, 0, 1, 0]
#n = 5
#arr = [1,1,1,1,1,1]
#n = 6


def sortZeroesAndOne(arr, n):
    i = 0
    j = n - 1
    while i < j:
        if arr[i] < arr[j]:
            i += 1
        elif arr[i] == arr[j]:
            if arr[i] == 1:
                while arr[j] >= arr[i] and i < j:
                    j -= 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
            else:
                while arr[i] <= arr[j] and i < j:
                    i += 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
                    j -= 1
        else:
            while arr[j] > arr[i]:
                j -= 1
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
            i += 1


sortZeroesAndOne(arr, n)
print(arr)
