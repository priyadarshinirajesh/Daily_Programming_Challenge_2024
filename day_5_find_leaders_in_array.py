'''
Given an array arr of size n. An element in considered a 
leader if it is greater than all the elements to its right.

We can find all such leader elements in array arr
using find_leaders function

Input :- array arr of n integers
Output :- result array containing all the leader elements

Time Complexity :- O(n)
Space Complexity :- O(n)
'''
def find_leaders(arr):
    if len(arr)<=1:
        return arr
    
    result = [arr[-1]]
    max_element = arr[-1]

    for i in range(len(arr)-2,-1,-1):
        if arr[i] > max_element:
            result.insert(0,arr[i])
            max_element = arr[i]

    return result

#test case 1
arr = [1,2,3,4,0]
print(find_leaders(arr))

#test case 2
arr = [7,10,4,10,6,5,2]
print(find_leaders(arr))

#test case 3
arr = [5]
print(find_leaders(arr))

#test case 4
arr = [100,50,20,10]
print(find_leaders(arr))

#test case 5
arr = [k for k in range(1,1000001)]
print(find_leaders(arr))

