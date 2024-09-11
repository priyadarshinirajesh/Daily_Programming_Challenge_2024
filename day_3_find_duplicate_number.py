'''
Given an array which contains n+1 integers
the elements in the array are in range [1,n]
It  is given that, there is exactly one duplicate number in array

The given code finds the duplicate number in the array
Time complexity : O(n)
where, n = number of elements in array
'''
def find_duplicate_number(arr):
    sum1 = 0
    for i in arr:
        sum1 += i

    n = len(arr)-1
    return sum1-(n*(n+1)//2)

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