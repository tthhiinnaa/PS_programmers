def solution(s):
    answer = True
    stack = 0
    for i in range(len(s)):
        if stack < 0:
            return False
        if s[i] == "(":
            stack += 1
        if s[i] == ")":
            stack -= 1
    if stack != 0:
        return False
    
    
    return True