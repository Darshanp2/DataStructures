class minHeap: 
    def __init__(self, capacity):
        self.storage = [0]* capacity;    #Creating minHeap of capacity
        self.capacity = capacity   #Capacity of minHeap
        self.size = 0                   #Current size 

    #Getting index of Parent, Left and Right child nodes
    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return 2*index + 1
    
    def getRightChildIndex(self, index):
        return 2*index + 2
    
    #Checking whether the index has Parent, Left and Right child nodes
    def hasParent(self, index): 
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    #Getting data of Parent, Left and Right child nodes
    def getParent(self, index):
        return self.storage[self.getParentIndex(index)]

    def getLeftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    #Checking whether the Heap is full or not 
    def isFull(self):
        return self.capacity == self.size
    
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    def insert(self, data):
        if(self.isFull()):
            return "Heap is full!"
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)
        
    def heapifyUp(self, index):
        if(self.hasParent(index) and self.getParent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMin(self):
        if self.size == 0:
            return "Heap is Empty!"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.storage[self.size-1] = 0
        self.size -= 1
        self.heapifyDown(0)
        return data

    def heapifyDown(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.getLeftChild(index) < self.storage[smallest]):
            smallest = self.getLeftChildIndex[index]
        
        if(self.hasRightChild(index) and self.getRightChildIndex(index) < self.storage[smallest]):
            smallest = self.getRightChildIndex[index]
        
        if smallest != index:
            self.swap(smallest, index)
            self.heapifyDown(smallest)

    #Displaying Heap and size of Heap
    def display(self):
        print("Heap:", self.storage)
        print("Size of Heap", self.size)

if __name__ == "__main__":
    a = minHeap(5)
    a.insert(4)
    a.insert(1)
    a.insert(0)
    d = a.removeMin()
    print(d)
    a.display()
                