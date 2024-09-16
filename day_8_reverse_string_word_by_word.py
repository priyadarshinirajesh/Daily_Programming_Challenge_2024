'''
Given a string s which consists of multiple words separated by spaces.
Task is to reverse the order of the words in the string.

Input:- string s of multiple words
Output:- result string, where the order of words are reversed

Time complexity:- O(n)
Space Complexity:- O(n)
'''
def reverse_string(s):
    arr = s.split()
    result = ""

    for i in range(len(arr)-1,-1,-1):
        result += arr[i]
        if i>0:
            result += " "

    result +=""
    return result

#test case1
s = "the sky is blue"
print(reverse_string(s))

#test case2
s = " hello world"
print(reverse_string(s))

#test case3
s = "a good  example"
print(reverse_string(s))

#test case4
s = "  "
print(reverse_string(s))

#test case5
s = "word"
print(reverse_string(s))
