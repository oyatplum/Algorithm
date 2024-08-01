import sys
input = sys.stdin.readline

count = int(input())
inputList = list(map(int, input().split()))
maxNum = max(inputList)
sum = 0

for i in range(count):
    inputList[i] = inputList[i]/maxNum*100
    sum += inputList[i]
print(sum/count)