def isPalindrome(src):
    if len(src) == 1:
        return True
    elif src[0] == src[-1]:
        smallString = src[1:len(src)-1]
        return True and isPalindrome(smallString)
    else:
        return False


src = "racecar"
res = str(isPalindrome(src))
print(res.lower())
