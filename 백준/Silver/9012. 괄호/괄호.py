import sys
input = sys.stdin.readline

N = int(input())
inputArr = []

for _ in range(N):
    inputArr.append(input().strip())

for i in inputArr:
    stack = []
    for j in i:
        if len(stack) == 0:
            stack.append(j)
            continue
        else:
            if ((j == ")" and stack[-1] == "(")):
                stack.pop()
            else:
                stack.append(j)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")