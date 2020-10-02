from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def heightOfTree(root):
    if root is None:
        return 0
    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))


def diameterOfBinaryTreeV2(root):
    # Your code goes here
    if root is None:
        return 0, 0
    # ans1 = heightOfTree(root.left) + heightOfTree(root.right)
    lh, ld = diameterOfBinaryTreeV2(root.left)
    rh, rd = diameterOfBinaryTreeV2(root.right)
    ht = 1 + lh + rh
    print(ht, ld, rd)
    return ht, max(ht + 1, ld, rd)

def diameterOfBinaryTree(root):
    # Your code goes here
    if root is None:
        return 0
    ans1 = heightOfTree(root.left) + heightOfTree(root.right)
    ans2 = diameterOfBinaryTree(root.left)
    ans3 = diameterOfBinaryTree(root.right)

    #print(ans1, ans2, ans3)
    return max(ans1+1, ans2, ans3)


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root == None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()

#print(diameterOfBinaryTree(root))
print(diameterOfBinaryTreeV2(root))
#diameterOfBinaryTreeV2(root)