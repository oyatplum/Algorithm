import sys
input = sys.stdin.readline
num = int(input())
total = 1
count = 0

for i in range(num):
    total *= i+1

listNum = list(reversed(str(total)))

for i in listNum:
    if i == '0':
        count += 1
    else:
        break
print(count)