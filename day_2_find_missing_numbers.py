def find_missing_number(arr):

    sum1 = 0
    for i in range(1,len(arr)+2):
        sum1 += i

    for i in arr:
        sum1 -= i

    return sum1


arr = [1,2,4,5]
print(find_missing_number(arr))

arr = [2,3,4,5]
print(find_missing_number(arr))

arr = [1,2,3,4]
print(find_missing_number(arr))

arr = [1]
print(find_missing_number(arr))

arr = [k for k in range(1,1000000)]
print(find_missing_number(arr))