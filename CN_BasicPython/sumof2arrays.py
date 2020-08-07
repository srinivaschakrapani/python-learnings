def sumOfTwoArrays(arr1, n, arr2, m, output):
    if n < m:
        n, m = m, n

    k = m - 1
    carry = 0

    outputsize = len(output) - 1
    for i in range(n - 1, -1, -1):
        if k != -1:
            s = arr1[i] + arr2[k] + carry
            sum = s % 10
            carry = s // 10
            output[outputsize] = sum
            outputsize -= 1
            k -= 1
        else:
            s = arr1[i] + carry
            sum = s % 10
            carry = s // 10
            output[outputsize] = sum
            outputsize -= 1
    if outputsize == 0:
        output[outputsize] = carry
    print(output)


arr1 = [6, 2, 4]
#arr1 = [8, 5, 2]
#arr1 = [9,7,6,1]
n = len(arr1)
arr2 = [7, 5, 6]
#arr2 = [1,3]
#arr2 = [4,5,9]
m = len(arr2)
outputSize = (1 + max(n, m))
output = outputSize * [0]
sumOfTwoArrays(arr1, n, arr2, m, output)
print(9761+459)
