import sys
input = sys.stdin.readline

N = int(input())
inputList = [0] * (10000 + 1)

for i in range(N):
    inputList[int(input())] += 1

for i in range(len(inputList)):
    if inputList[i] != 0:
        for _ in range(inputList[i]):
            print(i)