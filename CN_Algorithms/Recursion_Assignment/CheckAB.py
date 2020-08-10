'''a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
'''


def CheckAB(source):
    if len(source) == 0:
        return True
    if len(source) == 1 and source[0] == 'a':
        return True
    else:
        if source[0] == 'a':
            if source[1] == 'a' or source[1] == '':
                return True and CheckAB(source[1:])
            else:
                if source[1:3] == 'bb':
                    return True and CheckAB(source[3:])
                else:
                    return False
        else:
            if len(source) > 1:
                if source[1:2] == 'b':
                    return True and CheckAB(source[1:])
                else:
                    if source[1:3] == 'ba':
                        return True and CheckAB(source[3:])
                    else:
                        return False
            else:
                return False



src = "a" #True
#src = "abb" #True
print(str(CheckAB(src)).lower())
