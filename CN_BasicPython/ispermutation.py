## Read input as specified in the question.
## Print output as specified in the question.
import sys


def isPermutation(src, dest):
    ispermut = True
    if len(src) != len(dest):
        print("false")
    else:
        f = [0] * 255
        for i in src:
            f[ord(i)] += 1
        for j in dest:
            f[ord(j)] -= 1
        for k in f:
            if k != 0:
                ispermut = False
                break
        if ispermut:
            print("true")
        else:
            print("false")

# Taking Input Using Fast I/O
def takeInput():
    arr1 = str(sys.stdin.readline().rstrip())
    arr = str(sys.stdin.readline().rstrip())
    # if arr1 == '\'\'':
    #     arr1 = ' '
    # if arr == '\'\'':
    #     arr = ' '
    return arr1, arr


# main
# t = int(stdin.readline().rstrip())

# while t > 0 :

# arr, n = takeInput()

src, dest = takeInput()
# print(src)
isPermutation(src, dest)
# printList(arr, n)

# t -= 1
