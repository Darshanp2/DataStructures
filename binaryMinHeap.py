class minHeap:

    def __init__(self, capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size = 0

    #Defining Helper Methods
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0 
    
    def hasLeftChildIndex(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChildIndex(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        if self.size == self.capacity:
            return("Heap is Full")

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp 
    
    def insert(self, data):

        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while(self.hasParent(index) and self.parent(index) > self.storage[index]):  #getParentIndex(index)
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def removeMin(self):

        if(self.size) == 0:
            raise("Heap is Empty")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size-1] = 0
        self.size -= 1
        self.heapifyDown()
        return data
    
    def heapifyDown(self):

        index = 0 
        while(self.hasLeftChildIndex(index)):
            smallChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChildIndex(index) and self.rightChild(index) < self.leftChild(index)):
                smallChildIndex = self.getRightChildIndex(index)
            if(self.storage[index] < self.storage[smallChildIndex]):
                break
            else:
                self.swap(index, smallChildIndex)
            index = smallChildIndex
            print(smallChildIndex)

    def display(self):
        print(self.storage)
        print(self.size)

if __name__ == "__main__":
    a = minHeap(5)
    a.insert(2)
    a.insert(4)
    a.insert(3)
    d = a.removeMin()
    print(d)
    a.display()