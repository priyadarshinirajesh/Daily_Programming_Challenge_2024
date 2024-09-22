def permutations_of_string(s):
    if len(s)<=0:
        return ""
    
    if len(s) == 1:
        return [s]
    
    result = set()

    for i in range(len(s)):
        current_char = s[i]
        remaining = s[:i] + s[i+1:]

        for p in permutations_of_string(remaining):
            result.add(current_char + p)

    return list(result)

s = "abc"
print(permutations_of_string(s))

s = "aab"
print(permutations_of_string(s))

s = "aaa"
print(permutations_of_string(s))

s = "a"
print(permutations_of_string(s))

s = "abcd"
print(permutations_of_string(s))