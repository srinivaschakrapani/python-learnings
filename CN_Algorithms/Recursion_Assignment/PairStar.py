def PairStar(source):
    if len(source) == 1 or len(source) == 0:
        return source
    elif source[0] == source[1]:
        # If the adjacent characters are equal then print a * after first char and let
        # recursion takes care of the rest
        return source[0] + "*" + PairStar(source[1:])
    else:
        return source[0] + PairStar(source[1:])


src = input()
res = PairStar(src)
print(res)
