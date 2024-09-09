def sort_array_of_0s_1s_2s(arr):
    if len(arr)<=1:
        return arr
    
    if (1 not in arr and 2 not in arr) or (2 not in arr and 0 not in arr) or (0 not in arr and 1 not in arr):
        return arr
    
    low,mid = 0,0
    high = len(arr) - 1

    while mid <=high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
            mid += 1

    return arr

arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_array_of_0s_1s_2s(arr))

arr = [2, 2, 2, 2]
print(sort_array_of_0s_1s_2s(arr))

arr = [0,0,0,0]
print(sort_array_of_0s_1s_2s(arr))

arr = [1,1,1,1]
print(sort_array_of_0s_1s_2s(arr))

arr = [2,0,1]
print(sort_array_of_0s_1s_2s(arr))

arr = []
print(sort_array_of_0s_1s_2s(arr))

