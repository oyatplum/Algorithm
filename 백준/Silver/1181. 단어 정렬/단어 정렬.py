import sys

array = []
num = int(sys.stdin.readline())

if 1 <= num <= 20000:
    array = [input().strip() for _ in range(num)]

duplicateSortedArr = list(set(array)) #중복 단어 제거

lenSortedArr = sorted(duplicateSortedArr, key=lambda x: (len(x), x)) #문자열 길이로 정렬

for i in lenSortedArr:
    print(i)
