from itertools import permutations
import math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1
    
def solution(numbers):
    answer = 0
    temp = list(map(str, numbers))
    tempArr = set()
    
    for i in range(1, len(temp)+1):
        arr = permutations(temp, i)
        for a in arr:
            tempArr.add(a)
    
    tempNum = set()
    for target in tempArr:
        string = ''
        for i in target:
            string += i
        tempNum.add(int(string))
    
    for num in tempNum:
        if num >= 2:
            answer += isPrime(num)
        
    return answer