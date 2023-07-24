"""
Binary Search - also called as Interval Search

There are two approaches for Binary Search

1. Iterative Approach - Using loops
2. Recursive Approach - Recursively calling the method

Time Complexity:

Best Case: O(1)

Average Case: O(logN)

Worst Case: O(logN)

"""
def iterativeBinarySearch(arr, key, low, high):
    arr.sort()
    print(arr)
    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            high = mid - 1
        
        else:
            low = mid + 1
    return -1

def recursiveBinarySearch(arr, key, low, high):

    arr.sort()
    if low <= high:

        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid 
        
        elif key < arr[mid]:
            return recursiveBinarySearch(arr, key, low, mid - 1)
        
        else:
            return recursiveBinarySearch(arr, key, mid + 1, high)
    
    else:
        return -1 
    
if __name__ == "__main__":
    arr = [20,3,4,20,40]
    key = 20 

    result1 = iterativeBinarySearch(arr, key, 0, len(arr)-1)
    if result1 != -1:
        print("Key Found - Iterative Approach")
    else:
        print("Key not found - Iterative Approach")

    result2 = recursiveBinarySearch(arr, key, 0, len(arr) - 1)
    if result2 != -1:
        print("Key Found - Recursive Approach")
    else:
        print("Key not found - Recursive Approach")



