def solution(s):
    stack = []
    for x in s:
        if len(stack) > 0 and x == ')' and stack[-1] == '(':
            stack.pop()
            continue
        else:
            stack.append(x)
    if len(stack) > 0:
        return False
    else:
        return True