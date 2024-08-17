import sys
input = sys.stdin.readline

N = int(input())
A_List = set(map(int, input().split()))
M = int(input())
M_List = list(map(int, input().split()))

for i in M_List:
    if i in A_List:
        print("1")
    else:
        print("0")