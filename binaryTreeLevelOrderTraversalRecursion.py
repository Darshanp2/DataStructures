"""
Date: 1/18/2023

Core: Data Structures

Topic: Level Order Traversal in Binary Tree using RECURSION

"""

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevelOrder(root, i)

def printCurrentLevelOrder(root, level):
    if root is None:
        return 0
    if level == 1:
        print(root.data, end="")
    elif level > 1:
        printCurrentLevelOrder(root.left, level-1)
        printCurrentLevelOrder(root.right, level-1)
    
def height(node):
    if node is None:
        return 0
    else:
        lHeight = height(node.left)
        rHeight = height(node.right)
    
    if lHeight > rHeight:
        return lHeight+1 
    else:
        return rHeight+1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    printLevelOrder(root)