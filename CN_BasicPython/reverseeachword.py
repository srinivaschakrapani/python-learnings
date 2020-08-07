import sys
def reverseeachword(sent):
    words = sent.split(' ')
    reverse = ''
    for word in words:
        reverse += word[::-1]
        reverse += " "
    reverse = reverse.rstrip()
    print(reverse.rstrip())
    print(len(reverse))

def takeinput():
    arr = str(sys.stdin.readline().rstrip())
    return arr

sent =takeinput()
reverseeachword(sent)
print(len(sent))
#"Welcome to Coding Ninjas"