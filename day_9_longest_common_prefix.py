'''
Given an array of strings strs, consisting of lowercase letters.
Taskis to find the longest common prefix shared among all the strings.

Time complexity:- O(m*n)
where, n = number of words in array strs
        m = length of the shortest string in the array strs
Space Complexity:- O(1)
'''
def longest_common_prefix(arr):
    if not arr:
        return ""
    
    if len(arr)==1:
        return arr[0]

    min_ele = arr[0]

    for i in range(len(arr)):
        if len(arr[i])<len(min_ele):
            min_ele = arr[i]
    
    index = 0
    result = ""

    while index<len(min_ele):
        flag = 0
        for i in range(len(arr)):
            if arr[i][index] != min_ele[index]:
                flag = 1

        if flag == 0:
            result+=min_ele[index]
            index += 1
        else:
            break

    return result

#test case 1
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

#test case 2
strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))

#test case 3
strs = ["apple", "ape", "april"]
print(longest_common_prefix(strs))

#test case 4
strs = [""]
print(longest_common_prefix(strs))

#test case 5
strs = ["alone"]
print(longest_common_prefix(strs))
