import sys
input = sys.stdin.readline

total = int(input())
inputList = []

for i in range(total):
    inputList.append(int(input()))

inputList.sort()

for i in inputList:
    print(i)