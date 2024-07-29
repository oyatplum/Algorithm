import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cardList = list(map(int, input().split()))
sumList = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = cardList[i] + cardList[j] + cardList[k]
            if (sum <= M):
                sumList.append(sum)

sortedList = sorted(set(sumList), reverse=True)
print(sortedList[0])