import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * (T + 1)

for i in range(2, T + 1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[T])