import queue


def checkBalancedParanthesis(expr):
    supportedBrackets = ['{', '[', '(', ')', ']', '}']
    openBrackets = ['{', '[', '(']
    closedBrackets = ['}', ']', ')']
    s = queue.LifoQueue()  # Init a Stack
    for c in expr:
        if c in supportedBrackets:
            if s.empty() and c in closedBrackets:
                return False
                # s.put(s)
            elif s.empty() and c in openBrackets:
                s.put(c)
            else:
                # top_stack = s.get()
                if c in openBrackets:
                    s.put(c)
                else:
                    if not s.empty() and openBrackets.index(s.get()) == closedBrackets.index(c):
                        continue  # Do nothing
                    else:
                        return False
        else:
            continue
    if s.empty():
        return True
    else:
        return False


### Implement your code here

exp = input()
if checkBalancedParanthesis(exp):
    print('true')
else:
    print('false')

# { a + [ b+ (c + d)] + (e + f) }
