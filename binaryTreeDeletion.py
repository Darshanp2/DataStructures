"""
Date: 1/19/2023

Core: Data Structures - Trees

Topic: Deletion in a Binary Tree

"""
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end="")
    inorder(node.right)

def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return root
    keyNode = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            keyNode = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        
    if keyNode:
        x = temp.data
        deleteDeepest(root, temp)
        keyNode.data = x
    return root

if __name__ == "__main__":
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)

    inorder(root)
    deletion(root,5)

    print()
    inorder(root)