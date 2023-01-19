"""
Date: 1/18/2023

Core: Data Structure

Topic: Finding Height of a Binary Tree

"""

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    
def depth(node):
    if node is None:
        return 0
    
    else:

        lDepth = depth(node.left)
        rDepth = depth(node.right)

        if(lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the tree is ", depth(root))