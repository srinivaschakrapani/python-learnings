## Read input as specified in the question.
## Print output as specified in the question.
from sys import stdin


def tripleSum(arr, x):
    arr.sort()
    len_arr = len(arr)
    for i in range(0, len_arr - 1):
        start = i + 1
        end = len_arr - 1
        target_pair_sum = x - arr[i]
        while start < end:
            if arr[start] + arr[end] > target_pair_sum:
                end -= 1
            elif arr[start] + arr[end] < target_pair_sum:
                start += 1
            else:
                left_cnt = 0
                rt_cnt = 0
                for idx_left in range(start, end):
                    if arr[idx_left] == arr[start]:
                        left_cnt += 1
                    else:
                        break
                for idx_rt in range(end, start, -1):
                    if arr[idx_rt] == arr[end]:
                        rt_cnt += 1
                    else:
                        break
                target_pair_sum_count = left_cnt * rt_cnt
                if arr[start] == arr[end]:
                    target_pair_sum_count = ((end - start + 1) * (end - start)) // 2
                for k in range(0, target_pair_sum_count):
                    print(arr[i], end=" ")
                    print(arr[start], end=" ")
                    print(arr[end])
                start += 1
                end = end - rt_cnt


# def takeInput():
#     n = int(stdin.readline().rstrip())
#     if n == 0:
#         return list(), 0
#
#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     return arr, n
#

# arr, N = takeInput()
# target = int(input())
# tripleSum(arr, target)

#A = [1, 2, 3, 4, 5, 6, 7]
A = [2,2,2,2]
#target = 12
target = 6
tripleSum(A, target)
