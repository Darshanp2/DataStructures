"""

Linear Search 

Time Complexity: 

Best Case : O(1) - Key found at first index
Worst Case: O(N) - Key found at last index 
Average Case: O(N) 

"""

arr = [10,50,20,70,80,20,90,40]

flag = 0
key = 30 

for i in arr: 
    if i == key:
        print("Key found")
        flag = 1
        break

if flag != 1:
    print("Key not found")