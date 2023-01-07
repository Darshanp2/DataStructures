"""
Date: 1/5/2023

Core: Data Structures

Topic: Dynamic Array


""" 

class DynamicArray:

    #Initializing Constructor 
    def __init__(self):

        #Initializing Array to store elements
        #Initializing count to store the number of elements inserted
        #Initializing size of an array

        self.array = [0] * (1)
        self.count = 0
        self.size = 1


    #Method to add elements in array
    def add(self, data):

        #Checking whether the array has size 
        if(self.count == self.size):
            self.growSize()                  #if not call growsize to increase the size of an array
        
        self.array[self.count] = data
        self.count += 1

    def growSize(self):

        #Initialize new array "Temp" to increase the size of an array
        if(self.size == self.count):
            
            temp = [0] * (self.size * 2)
            i = 0 
            while(i < self.size):

                temp[i] = self.array[i]
                i += 1

            #Copying the temporary new array "temp" to the main array 
            self.array = temp 

            #Making the size double
            self.size = self.size*2
        
    
    def remove(self):

        if(self.count > 0):
            self.array[self.count-1] = 0 
            self.count -= 1

    def shrinkSize(self):

        temp = None
        #Initialize new array "temp" to decrease the size of an array
        
        if(self.count > 0):

            temp = [0] * (self.count)
            i = 0
            while(i < self.count):

                temp[i] = self.array[i]
                i += 1
            
            self.array = temp
            self.size = self.count

    def addAt(self,index,data):

        if(self.count == self.size):
            self.growSize()
        
        i = self.count - 1
        while(index <= i):
            self.array[i+1] = self.array[i]
            i -= 1

        self.array[index] = data
        self.count += 1
    
    def removeAt(self, index):

        if(self.count > 0):
            i = index

            while(i<self.count-1):

                self.array[i] = self.array[i+1]
                i += 1
            
            self.array[self.count-1] = 0
            self.count -= 1
        
    @staticmethod
    def main():

        da = DynamicArray()

        da.add(1)
        da.add(2)
        da.add(3)
        da.add(4)
        da.add(5)
        da.add(6)
        da.add(7)
        da.add(8)
        da.add(9)

        i = 0
        while(i<da.size):
            print(da.array[i])
            i += 1
        print()

        print("Size of an array", da.size)
        print("Number of elements in an array", da.count)

        da.shrinkSize()
        i = 0
        while(i<da.size):
            print(da.array[i])
            i += 1
        print()
        print("Size of an array", da.size)
        print("Number of elements in an array", da.count)
    
        da.addAt(4,45)
        i = 0
        while(i<da.size):
            print(da.array[i])
            i += 1
        print()
        da.shrinkSize()
        print("Size of an array", da.size)
        print("Number of elements in an array", da.count)

        da.remove()
        i = 0
        while(i<da.size):
            print(da.array[i])
            i += 1
        print()
        
        print("Size of an array", da.size)
        print("Number of elements in an array", da.count)

        da.removeAt(4)
        i = 0
        while(i<da.size):
            print(da.array[i])
            i += 1
        print()
        
        print("Size of an array", da.size)
        print("Number of elements in an array", da.count)


if __name__=="__main__":
    DynamicArray.main()
        
            


            

           
            