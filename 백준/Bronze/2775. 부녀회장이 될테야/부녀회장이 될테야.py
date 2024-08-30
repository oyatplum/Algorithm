import sys

input = sys.stdin.readline

T = int(input())
output = []

for i in range(T):
    K = int(input())
    N = int(input())
    Floor = [[0 for j in range(N)] for i in range(K + 1)]
    for k in range(N):
        Floor[0][k] = k + 1

    for j in range(1,K+1):
        for k in range(N):
            sum = 0
            for l in range(N):
                if k < l:
                    break
                else:
                    sum += Floor[j-1][l]
                    continue
            Floor[j][k] = sum
    output.append(Floor[K][N-1])

for i in output:
    print(i)