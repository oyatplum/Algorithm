import sys
input = sys.stdin.readline

inputArr = []
while True:
    inputString = input().rstrip("\n")
    if inputString == ".":
        break
    else:
        inputArr.append(inputString)

for i in inputArr:
    stack = []
    for j in i:
        if (j == "(" or j == ")" or j == "[" or j == "]") and len(stack) == 0:
            stack.append(j)
        else:
            if (j == ")" and stack[-1] == "(") or (j == "]" and stack[-1] == "["):
                stack.pop()
            elif (j == "(" or j == ")" or j == "[" or j == "]"):
                stack.append(j)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")