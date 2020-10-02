from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(preOrder, inOrder, n):
    if len(preOrder) == 0:
        return None
    # Find the root
    # Pre order = root -> Left -> right
    # Inorder = left -> root -> right
    root_data = preOrder[0]
    root_node = BinaryTreeNode(root_data)
    rootIndexInorder = inOrder.index(root_data)
    left_subtree_in = inOrder[:rootIndexInorder]
    right_subtree_in = inOrder[rootIndexInorder + 1:]

    leftSubTree_len= len(left_subtree_in)
    left_subtree_pre = preOrder[1:leftSubTree_len+1]
    right_subtree_pre = preOrder[leftSubTree_len+1: ]

    root_node.left = buildTree(left_subtree_pre, left_subtree_in, n-1)
    root_node.right = buildTree(right_subtree_pre, right_subtree_in,  n-1)

    return root_node


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)

'''
7
1 2 4 5 3 6 7 
4 2 5 1 6 3 7 

Output:
1 
2 3 
4 5 6 7 
'''