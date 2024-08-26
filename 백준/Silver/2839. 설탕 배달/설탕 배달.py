import sys
input = sys.stdin.readline

N = int(input())

big = 5
small = 3
output = 0

while N >= 0:
    if N % big == 0:
        output += N // big
        print(output)
        break
    N -= 3
    output += 1

else:
    print("-1")