"""
Date: 1/18/2023

Core : Data Structures

Topic : Binary Tree Traversals - InOrder, PreOrder, PostOrder

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
    

def printInorder(root):

    if root:
        printInorder(root.left)
    
        print(root.data, end = " ")

        printInorder(root.right)

def printPreorder(root):

    if root:
        print(root.data, end = " ")

        printPreorder(root.left)

        printPreorder(root.right)
    
def printPostorder(root):

    if root:
        printPostorder(root.left)

        printPostorder(root.right)

        print(root.data, end = " ")


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    printInorder(root)
    print()
    printPreorder(root)
    print()
    printPostorder(root)
    print()

    