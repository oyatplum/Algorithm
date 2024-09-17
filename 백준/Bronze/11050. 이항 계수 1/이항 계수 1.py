import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(a):
    b = 1
    for i in range(1, a+1):
        b *= i
    return b

output = factorial(N) // (factorial(K) * factorial(N - K))

print(output)