# Given a string mathematical expression, return true if redundant brackets are
# present in the expression. Brackets are redundant if there is nothing inside
# the bracket or more than one pair of brackets are present. Assume the given
# string expression is balanced and contains only one type of bracket i.e. ().
# Note: You will not get partial score for this problem. You will get marks only
# if all test cases are passed.
def checkRedundant(string):
    s = []
    for i in string:
        if i != ')':
            s.append(i)
        else:
            cnt = 0
            while len(s) != 0:
                k = s.pop()
                if k != '(':
                    cnt += 1
                else:
                    break
            if cnt == 0:
                return True
    return False

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')




