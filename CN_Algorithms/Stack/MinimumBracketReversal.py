def minimumbracketreversal(inp):
    if len(inp) % 2 == 1:
        return -1
    else:
        s = []
        for i in inp:
            if i == '{':
                s.append(i)
            else:
                if not isEmpty(s) and s[-1] == '{':
                    s.pop()  # Remove Balanced paranthesis incoming '{' , top = '}'
                else:
                    s.append(i)
        rev_count = 0
        while len(s) != 0:
            c2 = s.pop()  # This is a stack c2 comes first and then c1
            c1 = s.pop()
            if (c1 == '{' and c2 == '{') or (c1 == '}' and c2 == '}'):
                rev_count += 1
            elif c1 == '}' and c2 == '{':
                rev_count += 2
        return rev_count


def isEmpty(s):
    return len(s) == 0


inp = input()
res = minimumbracketreversal(inp)
print(res)
