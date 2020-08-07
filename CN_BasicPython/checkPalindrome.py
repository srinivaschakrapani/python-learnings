def checkPalindrome(num):
    i = num
    sum = 0
    while(i>0):
        k = i%10
        sum = sum*10 + k
        i = i//10
    if sum == num:
        return True
    return False

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
    print('true')
else:
    print('false')
