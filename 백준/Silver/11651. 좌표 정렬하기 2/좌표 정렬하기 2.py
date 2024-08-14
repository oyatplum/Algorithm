import sys
input = sys.stdin.readline

N = int(input())

coordinate = []

for _ in range(N):
    arr = []
    a, b = (map(int, input().split()))
    arr.append(a)
    arr.append(b)
    coordinate.append(arr)

coordinate.sort(key=lambda coordinate: (coordinate[1], coordinate[0]))

for i, j in coordinate:
    print(i,j)