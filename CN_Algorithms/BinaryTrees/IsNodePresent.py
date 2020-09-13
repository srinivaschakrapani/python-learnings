import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isNodePresent(root, x):
    # Given a Binary Tree and an integer x, check if node with data x is present
    # in the input binary tree or not. Return True or False.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return False
    if root.left is None and root.right is None:
        return root.data == x
    if not root.left is None and root.data == x:
        return True
    if not root.right is None and root.data == x:
        return True

    return isNodePresent(root.left, x) or isNodePresent(root.right, x)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
x = int(input())
present = isNodePresent(root, x)
if present:
    print('true')
else:
    print('false')
'''
1 2 3 -1 -1 -1 -1
2

1 -1 2 -1 3 -1 4 -1 5 -1 -1
1
'''
