import sys


def compressstr(inp):
    cons = 0
    prevchar = inp[0]
    for k in range(1, len(inp)):
        if inp[k] == prevchar:
            cons += 1
        else:
            if cons != 0:
                cons += 1
                # print(f"{inp[k - 1]}{cons}", end="")
                print("%s%s" % (inp[k - 1], cons), end='')
            else:
                # print(f"{inp[k - 1]}", end="")
                print("%s" % (inp[k - 1]), end='')
            cons = 0
        prevchar = inp[k]
    if cons > 0:
        cons += 1
        print("%s%s" % (prevchar, cons), end='')
    else:
        print("%s" % (prevchar), end='')


# aaabbccdsa
# aaabbccdsaaass
def takeinput():
    arr = str(sys.stdin.readline().rstrip())
    return arr


inp = takeinput()

compressstr(inp)
