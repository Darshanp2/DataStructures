"""
Quick Sort

Uses pivot and divides the array. Uses recursive calls to repeat the process on the smaller arrays.

Complexity: O(n^2)

""" 

def partition(arr, low, high):

    pivot = arr[low]
    start = low + 1
    end = high

    while True: 
        while start <= end and arr[end] >= pivot:
            end = end - 1 
        
        while start <= end and arr[start] <= pivot: 
            start = start + 1

        if start <= end: 
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    
    arr[low], arr[end] = arr[end], arr[low]

    return end 


def quick_sort(arr, low, high):

    if low <= high: 
        idx = partition(arr, low, high)

        quick_sort(arr, low, idx - 1)
        quick_sort(arr, idx + 1, high)

if __name__ == "__main__":
    arr = [7, 6, 10, 5, 2, 1, 15]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)