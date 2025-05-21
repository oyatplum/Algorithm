def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            poped = stack.pop()
            if i == "(":
                stack.append(poped)
                stack.append(i)
                    
            if i == ")":
                if poped == "(":
                    continue
                else:
                    stack.append(poped)
                    stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False