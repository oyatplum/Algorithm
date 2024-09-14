import sys
input = sys.stdin.readline

N = int(input())
cardList = list(map(int, input().split()))

M = int(input())
numList = list(map(int, input().split()))

diction = {}

for card in cardList:
    if card in diction:
        diction[card] += 1
    else:
        diction[card] = 1

for num in numList:
    result = diction.get(num)
    if result == None:
        print("0", end=" ")
    else:
        print(result, end=" ")