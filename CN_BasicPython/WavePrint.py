from sys import stdin


def wavePrint(mat, nRows, mCols):
    # Your code goes here
    for j in range(mCols):
        x, y, i = 0, nRows, 1
        if j % 2 == 1:
            x, y, i = nRows - 1, -1, -1
        for k in range(x, y, i):
            print(mat[k][j], end =' ')


# Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
