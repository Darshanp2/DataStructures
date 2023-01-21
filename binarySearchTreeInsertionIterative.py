"""
Date: 1/20/2023

Core: Data Structure - Binary Search Tree

Topic - Deletion in a Binary Search Tree

Complexity - O(logn)

"""

class newNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(temp):
    if temp is None:
        return
    inorder(temp.left)
    print(temp.data,end=" ")
    inorder(temp.right)

def insert(root,key):
    if root is None:
        root = newNode(key)
        return 
    node = newNode(key)
    prev = None
    temp = root
    while(temp != None):
        if(temp.data < key):
            prev = temp
            temp = temp.right
        else:
            prev = temp
            temp = temp.left
        
    if prev.data > key:
        prev.left = node
    else:
        prev.right = node
    
if __name__ == "__main__":
    root = newNode(1)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 4)
    print(root)
    inorder(root)