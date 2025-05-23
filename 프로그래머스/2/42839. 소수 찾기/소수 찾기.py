from itertools import permutations
import math
def isPrime(target):
    for i in range(2, int(math.sqrt(target) + 1)):
        if target % i == 0:
            return 0
    return 1
    
def solution(numbers):
    answer = 0
    numArr = []
    for i in numbers:
        numArr.append(i)
    
    perSet = set()
    
    for i in range(1, len(numArr)+1):
        temp = set(permutations(numArr, i))
        for t in temp:
            perSet.add(t)
    
    resultSet = set()
    
    for per in perSet:
        string = ''
        for p in per:
            string += p
        resultSet.add(int(string))
    
    for i in resultSet:
        if i < 2:
            continue
        else:
            answer += isPrime(i)
    return answer