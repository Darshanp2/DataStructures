"""
Date: 1/21/2023

Core: Data Structures - Binary Search Tree

Topic: Deletion in a Binary Search Tree using Recursion

Complexity: O(logn)

Recursive method

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
    print(temp.data, end=" ")
    inorder(temp.right)

def insert(root, key):

    if root is None:
        root = newNode(key)
        return root
    if root is key:
        return root
    
    if(key < root.data):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    return root

def search(root, key):
    if root is None:
        return None
    else:
        if root.data is key:
            return root.data
        else:
            if key < root.data:
                return search(root.left, key)
            else:
                return search(root.right, key)

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.data = temp.data

        root.right = deleteNode(root.right, temp.data)

        return root 

def minValueNode(node):
    current = node

    while(current.left != None):
        current = current.left
    
    return current

if __name__ == "__main__":

    root = newNode(4)
    insert(root, 2)
    insert(root, 3)
    insert(root, 5)
    print()
    inorder(root)
    deleteNode(root, 4)
    print()
    inorder(root)