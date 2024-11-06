import sys
input = sys.stdin.readline

N, M = map(int, input().split())

NSet = set()
output = set()

for _ in range(N):
    NSet.add(input().strip())

for _ in range(M):
    notSeen = input().strip()
    if notSeen in NSet:
        output.add(notSeen)
    else:
        continue

print(len(output))
for i in sorted(output):
    print(i)