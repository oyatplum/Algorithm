from itertools import combinations

def solution(nums):
    answer = 0
    maxLen = len(set(nums))
    numLen = len(nums)//2
    
    if maxLen < numLen:
        answer = maxLen
    else:
        answer = numLen
    
    return answer