# first variant
def islistsorted(lst):
    print(id(lst))
    if len(lst) == 0 or len(lst) == 1:
        return True
    if lst[0] <= lst[1]:
        return islistsorted(lst[1:])
    else:
        return False


def islistsortedbetterversion(lst, start):
    print(id(lst))
    len_lst = len(lst)
    if start == len_lst - 1:
        return True
    if lst[start] > lst[start + 1]:
        return False
    return islistsortedbetterversion(lst, start + 1)


lst = [1, 2, 3, 4, 5, 6, 22,-1]
# print(id(lst))
# print(islistsorted(lst))
print(islistsortedbetterversion(lst, 0))
