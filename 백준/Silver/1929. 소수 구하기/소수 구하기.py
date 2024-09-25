import math
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [True for i in range(N+1)]
arr[0] = arr[1] = False

for i in range(2, int(math.sqrt(N)) +1):
    if arr[i] == True:
        j = 2
        while True:
            if i*j <= N:
                arr[i*j] = False
                j += 1
                continue
            break

for j in range(M, N+1):
    if arr[j] == True:
        print(j)