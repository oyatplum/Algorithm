import sys
input = sys.stdin.readline

inputNum = int(input())

if inputNum == 1:
    print("1")
else:
    level = 1
    while True:
        if inputNum <= 3*level*(level+1) + 1:
            print(level+1)
            break
        else:
            level += 1
            continue