'''
Given two sorted arrays arr1 of size m and arr2 of size n.
Task is to merge these two arrays into a single sorted array without
using any extra space. 

Input : arr1 of size m and arr2 of size n
Output : arr1 contains first part of merged array and arr2 contains second part of merged array

Time Complexity : O((m+n)log(m+n))
Space Complexity : O(1)

'''

def heapify(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
        
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,i,0)
    
def sort_arrays(arr1,arr2):

    i = len(arr1)-1
    j = 0

    while i>=0 and j<len(arr2):
        if arr1[i]>arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]

        i-=1
        j+=1

    heap_sort(arr1)
    heap_sort(arr2)

    return arr1,arr2

# test case 1
arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
print(sort_arrays(arr1,arr2))

# test case 2
arr1 = [10,12,14]
arr2 = [1,3,5]
print(sort_arrays(arr1,arr2))

# test case 3
arr1 = [2,3,8]
arr2 = [4,6,10]
print(sort_arrays(arr1,arr2))

# test case 4
arr1 = [1]
arr2 = [2]
print(sort_arrays(arr1,arr2))



