import sys
input = sys.stdin.readline

n = 0
for i in range(3,0,-1):
    x = input().strip()
    if x.isdigit():
        n = int(x) + i

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0 and not(n % 5 == 0):
    print("Fizz")
elif not(n % 3 == 0) and n % 5 == 0:
    print("Buzz")
else:
    print(n)