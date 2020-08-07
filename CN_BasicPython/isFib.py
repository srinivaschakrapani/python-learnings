def checkMember(n):
    f = 1
    s = 1
    isFib = False
    if n == 1:
        isFib = True
        return isFib
    while n>0:
        nxt = f + s
        f=s
        s=nxt
        if n == nxt:
            isFib = True
            break
        elif nxt > n:
            isFib = False
            break
    return isFib

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")