"""

Bubble Sort

Time Complexity : O(N^2)

"""

arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
n = len(arr)

for i in range(n):
    swapped = False

    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
            swapped = True

    if swapped == False:
        break

print(arr)
         

