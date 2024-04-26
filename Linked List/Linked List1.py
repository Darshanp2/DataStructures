#Implementation of Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def traverse(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next

    def insertBeg(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return 
    
        traversalNode = self.head
        while(traversalNode.next) :
            traversalNode = traversalNode.next
        
        traversalNode.next = newNode

    def insertAfter(self, data, insertAfterData):
        
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
    
        prevNode = self.head

        while(prevNode.data != insertAfterData):
            prevNode = prevNode.next
        
        if(prevNode.data == insertAfterData):
            newNode.next = prevNode.next
            prevNode.next = newNode
        else:
            return "Node not found in the Linked List"

    #Finding the length of the Linked List 

    #Iterative Approach
    def getLengthIterative(self):
        if self.head is None:
            return "No Node in the Linked List"
        else:
            count = 0
            traversalNode = self.head
            while(traversalNode.next):
                count += 1
                traversalNode = traversalNode.next
            return count 
    
    #Recursive Approach
    def getLengthRecursive(self):
        if self.head is None:
            return "No Node in the Linked List"
        else: 
            return self.getCountRecursive(self.head)
            
    def getCountRecursive(self, node):
        if (not node):
            return 0
        else:
            return 1 + self.getCountRecursive(node.next)
        

    #Searching Element in the Linked List

    #Using Vector to find element
    def searchElement(self, element):
        if self.head is None:
            return "No Element in the Linked List"
        else:
            v = []
            temp = self.head
            while(temp):
                v.append(temp.data)
                temp = temp.next
            
            if element in v:
                print("Element found in the linked list")
            else:
                print("Element not found in the linked list")

    #Searching using Iterative Approach
    def searchElementIteratively(self, element):
        if self.head is None:
            print("No Element present in the Linked list")
        else:
            flag = 0
            traversalNode = self.head
            while(traversalNode.next is not None):
                if element == traversalNode.data:
                    flag = 1
                    print("Element present in the Linked List")
                    break
                else:
                    traversalNode = traversalNode.next
            
            if flag == 0:
                print("Element not present in the Linked List")

    def searchElementRecursively(self, element):
        if self.head is None:
            print("No Element present in the Linked list")
        else:
            print(self.getSearchCount(self.head, element))

    def getSearchCount(self, node, element):
        if (node.data == element):
            return "Element found"
        elif(not node):
            return("Element not found")
        else:
            return(self.getSearchCount(node.next, element))

    #Deleting Node 

    def deleteNode(self, node):
        if (self.head is None):
            return "No Element in the Linked List"
        else:
            traversalNode = self.head
            prevNode = traversalNode
        #
        #
        #
        #

llist1 = LinkList()
llist1.head = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

llist1.head.next = e2
e2.next = e3

#Inserting at the Beginning, at End and Inserting After a given node
print("Inserting at Beginning")
llist1.insertBeg("Sun")
llist1.traverse()

print("Inserting at End")
llist1.insertEnd("Fri")
llist1.traverse()

print("Inserting After")
llist1.insertAfter("Thu","Wed")
llist1.traverse()

#Finding Length of Linked List Recursively and Iteratively
print("Getting Length Iteratively", llist1.getLengthIterative())
print("Getting Length Recursively", llist1.getLengthRecursive())

#Searching Element
llist1.searchElement("Sat")
llist1.searchElementRecursively("Tue")




