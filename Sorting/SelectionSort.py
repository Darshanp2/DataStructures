"""

Selection Sort

Time Complexity: O(N^2)

"""

arr = [9, 25, 12, 9, 11]

for i in range(len(arr)):
    min_idx = i 
    
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j

    arr[min_idx], arr[i] = arr[i], arr[min_idx]

print(arr)