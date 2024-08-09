import sys
input = sys.stdin.readline

alphaList = [chr(c) for c in range(97,123)]

L = int(input())
stringList = list(input().strip())

sum = 0
M = 1234567891

for i in range(L):
    for j in alphaList:
        if stringList[i] == j:
            sum = sum + ((alphaList.index(j) + 1)*(31**i))

print(sum % M)