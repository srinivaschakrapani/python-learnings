'''
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))

'''

from sys import stdin


def findLargest(arr, nRows, mCols):
    # Your code goes here
    maxSum = -2147483648
    colIdex = -1
    maxColSum = -2147483648
    colSum = 0
    maxColIdex = -1
    for j in range(mCols):
        for ele in arr:
            colSum += ele[j]
            colIdex = j
        if colSum > maxColSum:
            maxColSum = colSum
            maxColIdex = colIdex
        colSum = 0

    rowIdex = -1
    maxRowSum = -2147483648
    rowSum = 0
    maxRowIdex = -1
    for i in range(nRows):
        for j in range(mCols):
            rowSum += arr[i][j]
            rowIdex = i
        if rowSum > maxRowSum:
            maxRowSum = rowSum
            maxRowIdex = rowIdex
        rowSum = 0
    if maxColSum > maxRowSum:
        print(f"column {maxColIdex}, {maxColSum}")
    elif maxRowSum != maxSum:
        print(f"row {maxRowIdex}, {maxRowSum}")
    else:
        print(f"row 0, {maxRowSum}")

# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
