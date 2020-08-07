def replacechar(s, a, b):
    print(s, len(s))
    if len(s) == 0:
        return s

    smalloutput = replacechar(s[1:], a, b)
    print(f"Small output --> {smalloutput} And S --> {s}")
    if s[0] == a:
        return b + smalloutput
    else:
        return s[0] + smalloutput

s = "XABXCX"
print(replacechar(s, 'X', 'A'))