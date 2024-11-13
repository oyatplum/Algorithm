import sys
input = sys.stdin.readline

zeroCount = [1,0,1]
oneCount = [0,1,1]

T = int(input())

def fibo(n):
    length = len(zeroCount)
    if n >= length:
        for i in range(length, n+1):
            zeroCount.append(zeroCount[i-1] + zeroCount[i-2])
            oneCount.append(oneCount[i-1] + oneCount[i-2])
    print(zeroCount[n], oneCount[n])

for _ in range(T):
    n = int(input())
    fibo(n)