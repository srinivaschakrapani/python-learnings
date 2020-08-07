import sys


def removeconsecutivedups(inp):
    if len(inp) <= 1:
        print(inp)
    else:
        output=inp[0]
        for k in range(1,len(inp)):
            if inp[k-1] == inp[k]:
                continue
            else:
                output+=inp[k]
    print(output)


# def takeInput():
#     inp = str(sys.stdin.readline().rstrip())
#     return inp
#inp = "aabccbaa"
inp ="xxyyzxx"
removeconsecutivedups(inp)