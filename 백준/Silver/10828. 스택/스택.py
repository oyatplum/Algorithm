import sys
input = sys.stdin.readline

N = (int(input()))
stack = []
output = []

for _ in range(N):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            output.append("-1")
        else:
            output.append(stack.pop())
    elif command[0] == "size":
        output.append(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            output.append("1")
        else:
            output.append("0")
    elif command[0] == "top":
        if len(stack) == 0:
            output.append("-1")
        else:
            output.append(stack[-1])

for i in output:
    print(i)