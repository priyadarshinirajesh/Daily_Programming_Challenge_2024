'''
Given an array which contains n+1 integers
the elements in the array are in range [1,n]
It  is given that, there is exactly one duplicate number in array

The given code finds the duplicate number in the array using find_duplicate_number function
Time complexity should be O(n)
where, n = number of elements in array
'''
def find_duplicate_number(arr):
    '''
    This functions is used to find the duplicate number in the array

    arg: arr(list) - array containing the numbers
    return: int - returns the duplicate number in the array

    Time complexity : O(n)
    Space complexity : O(1)
    '''
    
    for i in range(len(arr)):
        index = abs(arr[i]) - 1

        if arr[index] < 0:
            return abs(arr[i])
        
        arr[index] = -arr[index]
        

#test case 1
arr = [1,3,4,2,2]
print(find_duplicate_number(arr))

#test case 2
arr = [3,1,3,4,2]
print(find_duplicate_number(arr))

#test case 3
arr = [1,1]
print(find_duplicate_number(arr))

#test case 4
arr = [1,4,4,2,3]
print(find_duplicate_number(arr))

#test case 5
arr = [k for k in range(1, 100000)]
arr.append(50000)
print(find_duplicate_number(arr))