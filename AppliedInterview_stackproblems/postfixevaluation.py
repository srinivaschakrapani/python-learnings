class Stack:
    def __init__(self):
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if not self.isempty:
            return self.stack.pop()
        return -1

    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        return -1


if __name__ == '__main__':
    s = Stack()
    s.push(23)
    s.push(21)
    s.push(12)
    print(s.peek())
    print(s.pop())
    print(s.peek())
# def EvaluatePostFix(expr):


# def Priority:
