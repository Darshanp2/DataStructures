class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def insert(root, newNode):
    #No node is present in the tree. Returning the node as a root node
    if root is None:
        return Node(newNode)
    else:
    #If the node is already present then returning it back
        if root.val == newNode:
            return root
        #If the new node is less than the Root node, then calling the same method with root.left
        elif newNode < root.val:
            root.left = insert(root.left, newNode)
        #If the new node is greater than the Root node, then calling the same method with root.right
        else:
            root.right = insert(root.right, newNode)

    return root 

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
    
def search(root, node):
    if root is None or root.val == node:
        return root

    if node < root.val:
        return search(root.left, node)
    else:
        return search(root.right, node)
    
def deleteNode(root, node):
    #if root is None
    if root is None:
        return root
    #Traversing by comparing the root's value with the value to be deleted
    if node < root.val:
        root.left = deleteNode(root.left, node)
    elif node > root.val:
        root.right = deleteNode(root.right, node)
    #Node to be deleted is identified as Root Node and that Root node only has one child 
    else:
        #Returning other child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        #Node to be deleted is Root Node and that Root Node has two children 
        #Calling minValue method to find the min left node of right child
        root.val = minValue(root.right)     #Replacing Root's value with min left child node

        root.right = deleteNode(root.right, root.val)       #Deleting the min left child from the tree      
    
    return root

def minValue(root):
    minVal = root.val
    while root.left:
        minVal = root.left.val
        root = root.left
    return minVal
            
if __name__ == "__main__":
    root = Node(50)
    root = insert(root,30)
    root = insert(root,70)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,60)
    root = insert(root,80)
    root = insert(root,85)
    inorder(root)

    s = search(root,30)
    print("\n")
    if s is None: 
        print("Node not found")
    else: 
        print(s.val, "Found")
    
    d = deleteNode(root, 50)
    inorder(root)
    
