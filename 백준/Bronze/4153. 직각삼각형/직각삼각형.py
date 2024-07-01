import sys
answer = []

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    a, b, c = sorted([a, b, c])
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if 0 < a < 30000 and 0 < b < 30000 and 0 < c < 30000:
            if a**2 + b**2 == c**2:
                answer.append("right")
            else:
                answer.append("wrong")
                continue
for i in answer:
    print(i)