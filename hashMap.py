"""

Date: 1/7/2023

Core: Data Structures

Topic: HashMap

""" 

class hashTable:

    def __init__(self):
        self.MAX = 10                          #Initializing maximum value of array to 100 
        self.arr = [[] for i in range(self.MAX)]                #Initializing Arrays for individual elements in order to avoid collision

    def get_hash(self, key):                    
        h = 0
        for char in key:
            h += ord(char)                      #ord gives us ASCII value for that character
        
        a = h % self.MAX
        return a
    
    def setValue(self, key, value):

        h = self.get_hash(key)
        found = False         
        for idx, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h][idx] = [key, value]             #Replacing the old value with the new value if the key is same
                found = True

        if found == False:
            self.arr[h].append([key, value])
    
    def getValue(self, key):

        h = self.get_hash(key)
        return self.arr[h]                      #Retrieving the value from the hashed value's location
    
    def delValue(self, key):

        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

if __name__ == "__main__":
    t = hashTable()
    t.setValue('march 6', 310)
    t.setValue('march 1', 23)
    t.setValue('march 2', 189)
    t.setValue('march 17', 63457)
    t.setValue('march 8', 1)
    t.setValue('march 8', 2)
    a = t.getValue('march 69')
    d = t.delValue('march 8')
    print(t.arr)
    print(a)
    
