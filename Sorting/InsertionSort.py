"""
Insertion Sort

Time Complexity: O(n^2)

"""

data = [9, 5, 1, 4, 3]

for step in range(1, len(data)):
    key = data[step]
    j = step -1 
    while j >= 0 and key < data[j]:
        data[j+1] = data[j]
        j -= 1
    data[j+1] = key 

print(data)






