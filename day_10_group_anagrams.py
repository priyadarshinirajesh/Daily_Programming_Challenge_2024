'''
Given an array of string strs[]. Task is to group all the strings
that are anagrams of each other.

Time complexity:- O(m*n*log(m))
Space complexity:- O(m*n)
'''
def group_anagrams(arr):
    if len(arr)<=0:
        return []
    
    d = {}

    for i in range(len(arr)):
        k = str(sorted(list(arr[i])))
        if k in d.keys():
            d[k].append(arr[i])
        else:
            d[k] = [arr[i]]
    
    result = []
    for k in d.values():
        result.append(k)

    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))

strs = [""]
print(group_anagrams(strs))

strs = ["a"]
print(group_anagrams(strs))

strs = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
print(group_anagrams(strs))

strs = ["abc", "def", "ghi"]
print(group_anagrams(strs))