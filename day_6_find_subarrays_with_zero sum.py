'''
Given an integer array arr of size n.
Find all the subarrays whose sum is zero

Input:- array arr of size n
Output:- result array containing the starting and ending indices of subarrays
having zero as their sum

Time complexity: - O(n)
Space complexity:- O(n)

'''
def subarray_with_zero(arr):
    result = []
    current_sum = 0
    indices = {0:[-1]}

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum in indices:
            for start in indices[current_sum]:
                result.append((start+1,i))

        if current_sum in indices:
            indices[current_sum].append(i)
        else:
            indices[current_sum] = [i]

    return result

# Test cases
n = int(input("enter the size of the array:"))
arr = []
for i in range(n):
    arr.append(int(input()))

print(subarray_with_zero(arr))
