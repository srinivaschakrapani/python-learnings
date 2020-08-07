def removedups(string):
    if len(string) == 0 or len(string) == 1:
        return string
    if string[0] == string[1]:
        return removedups(string[1:])
    else:
        return string[0] + removedups(string[1:])

s = "aabccba" #abcba
print(removedups(s))