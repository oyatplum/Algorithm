import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

if a >= v:
    print("1")
else:
    if (v-b) % (a-b) == 0:
        print((v-b) // (a-b))
    else:
        print((v-b) // (a-b) + 1)