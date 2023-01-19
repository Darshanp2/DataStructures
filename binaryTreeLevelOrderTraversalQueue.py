"""
Date: 01/18/2023

Core: Data Structures - Tress

Topic : Level Order Traversal in a Binary Tree using Queue 

Time Complexity : O(n)

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return 0
    
    q = []
    q.append(root)

    while(len(q) > 0):
        print(q[0].data, end="")
        node = q.pop(0)
        
        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)