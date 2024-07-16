import sys
input = sys.stdin.readline

inputArr = []

while True:
    a = int(input())
    if a == 0:
        break
    else:
        inputArr.append(a)

for i in inputArr:
    if str(i) == str(i)[::-1]:
        print("yes")
    else:
        print("no")