from random import randint


# Approach 1 : rotate array 1 at a time d times
# Appriach 2 : copy elements from 1 to d and then copy the elements
#Approach 3:
    # Reverse the array
    # Reverse the elements from 0, n-1-d
    # Reverse the elements from (n-1-d) + 1 to n-1
    # 0 1 2 3 4 5
    # 2 3 4 5 6 7 rotate at d = 3
    # reverse the array
    # 7 6 5 4 3 2


def rotate(arr, n, d):
    reverse(arr, 0, n - 1)
    reverse(arr, 0, n - 1 - d)
    reverse(arr, n - d, n - 1)
    print('Rotate' , arr)


# def reverse(arr, st, end):
#     if st >= end:
#         return
#     # temp = arr[st]
#     # arr[st] = arr[end]
#     # arr[end] = temp
#     arr[st], arr[end] = arr[end], arr[st]
#     return reverse(arr, st+1, end-1)
def reverse(arr, start, end):
    if start >= end:
        return
    else:
        length = end - start + 1
        for i in range(length // 2):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    #print(arr)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr)
# arr = [ randint(1,10) for i in range(1000)]
# rotate(arr, len(arr), 8)
reverse(arr, 2, 4)
print(arr)
