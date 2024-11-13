import sys
input = sys.stdin.readline

N, K = map(int, input().split())

count = 0
coin = []

for i in range(N):
    coin.append(int(input().strip()))
    
coin.reverse()

for i in coin:
    if K >= i:
        count += K // i
        K = K - (i * (K // i))
        continue
    else:
        continue
print(count)