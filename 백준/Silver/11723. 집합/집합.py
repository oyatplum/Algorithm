import sys
input = sys.stdin.readline

N = int(input())
inputSet = set()

for _ in range(N):
    str_input = input().split()
    command = str_input[0]
    if len(str_input) == 2:
        num = int(str_input[1])

        if command == "add":
            inputSet.add(num)
        elif command == "remove":
            inputSet.discard(num)
        elif command == "check":
            if num in inputSet:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if num in inputSet:
                inputSet.discard(num)
            else:
                inputSet.add(num)
    else:
        if command == "all":
            inputSet = set()
            for i in range(1,21):
                inputSet.add(i)
        elif command == "empty":
            inputSet = set()
