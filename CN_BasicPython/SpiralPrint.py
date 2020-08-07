from sys import stdin


def spiralPrint(mat, nRows, mCols):
    rs = 0
    rend = nRows
    cs = 0
    cend = mCols

    while rs < nRows and cs < mCols:
        # Direction -->
        for j in range(cs, cend):
            print(mat[rs][j], end=" ")
        rs += 1

        # Direction Down
        for j in range(rs, rend):
            print(mat[j][cend - 1], end=" ")
        cend -= 1

        # Direction <---
        for j in range(cend-1, cs-1, -1):
            print(mat[rend-1][j], end=" ")
        rend -= 1

        # Direction top
        for j in range(rend-1, rs - 1, -1):
            print(mat[j][cs], end=" ")
        cs += 1


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
