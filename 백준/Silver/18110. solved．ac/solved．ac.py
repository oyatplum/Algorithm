import sys
input = sys.stdin.readline

N = int(input())
inputList = []

def roundFunc(num):
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

if N == 0:
    print(0)
else:
    for _ in range(N):
        inputList.append(int(input()))
    percent = roundFunc(N*0.15)
    inputList.sort()
    inputList = inputList[percent:N-percent]
    average = roundFunc(sum(inputList) / len(inputList))
    print(average)