import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def numOfLeafNodes(root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return 1
    numOfLeft = numOfLeafNodes(root.left)
    numOfRight = numOfLeafNodes(root.right)
    return numOfLeft + numOfRight


def buildLevelTree():
    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
root = buildLevelTree()
print(numOfLeafNodes(root))
