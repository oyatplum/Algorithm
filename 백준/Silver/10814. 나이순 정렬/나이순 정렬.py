import sys
input = sys.stdin.readline

inputNum = int(input())
person_list = []

for i in range(inputNum):
    person = []
    a, b = map(str, input().split())
    person.append(int(a))
    person.append(b)
    person_list.append(person)

person_list.sort(key=lambda person_list: person_list[0])


for per in person_list:
    for i in per:
        print(i, end=" ")
    print(sep="\n")