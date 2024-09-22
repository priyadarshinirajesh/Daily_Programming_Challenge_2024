def valid_parenthesis(s):
    if len(s)<=0:
        return True
    
    stack = []
    for i in range(len(s)):
        if s[i] in "[{(":
            stack.append(s[i])
        elif stack and s[i]==")" and stack[-1] =="(":
            stack.pop()
        elif stack and s[i]=="}" and stack[-1] =="{":
            stack.pop()
        elif stack and s[i]=="]" and stack[-1] =="[":
            stack.pop()
        else:
            return False
        
    if not stack:
        return True
    else:
        return False

s = "()"
print(valid_parenthesis(s))
s = "([)]"
print(valid_parenthesis(s))
s = "[{()}]"
print(valid_parenthesis(s))
s = ""
print(valid_parenthesis(s))
s = "{[}"
print(valid_parenthesis(s))
