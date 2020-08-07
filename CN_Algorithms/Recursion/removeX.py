def removeX(string):
    if len(string) == 0:
        return string
    smalloutput = removeX(string[1:])
    if string[0] == 'X':
        return ''.join(smalloutput)
    else:
        return string[0] + smalloutput


s = "XXX"
print(removeX(s))
