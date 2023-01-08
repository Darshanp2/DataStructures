"""
Date: 1/7/2023

Core: Data Structures

Topic: Singly Linked List

""" 

#Creating a node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    #Inserting a node at the beginning of the Linkedlist
    def insertBeg(self, data):

        #Creating the new node
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode
    
    #Adding a node after a given node
    def insertAfter(self, prevNode, data):

        if prevNode is None:
            print("The given previous node must be present in Linked List")
            return
        
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    #Adding a node at the end of the Linked List

    def insertEnd(self, data):

        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = newNode

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        
if __name__ == "__main__":
    llist = Linkedlist()

    llist.insertEnd(3)
    llist.insertEnd(4)

    llist.insertAfter(llist.head,5)
    llist.insertBeg(1)
    llist.printlist()
