import queue


class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWiseBinaryTree(root):
    # Your code goes here
    q = queue.Queue()
    if root is None:
        return
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, ":", sep='', end='')
        if current_node.left is None:
            print("L:-1",sep='',end=',')
        else:
            print("L:", current_node.left.data, sep='', end=",")
            q.put(current_node.left)
        if current_node.right is None:
            print("R:", -1, sep='', end="")
        else:
            print("R:", current_node.right.data, sep='', end="")
            q.put(current_node.right)
        print()


def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root")
    root_data = int(input())
    if root_data == -1:
        return None
    root = BinaryTree(root_data)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("enter left child of ", current_node.data)
        left_child_data = int(input())
        if left_child_data != -1:
            left_child = BinaryTree(left_child_data)
            current_node.left = left_child
            q.put(left_child)
        print("enter right child of ", current_node.data)
        right_child_data = int(input())
        if right_child_data != -1:
            right_child = BinaryTree(right_child_data)
            current_node.right = right_child
            q.put(right_child)
    return root


root = takeLevelWiseTreeInput()
printLevelWiseBinaryTree(root)
