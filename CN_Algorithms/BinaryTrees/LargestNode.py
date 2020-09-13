import queue
from queue import Queue
class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildLevelTree(levelorder):
    index = 0
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


def LargestNode(root):
    if root is None:
        return -1
    left_large = LargestNode(root.left)
    right_large = LargestNode(root.right)
    return max(left_large, right_large, root.data)


levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = LargestNode(root)
print(k)
