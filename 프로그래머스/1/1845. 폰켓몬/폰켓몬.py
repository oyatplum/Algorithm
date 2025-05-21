def solution(nums):
    selectNum = len(nums) // 2
    kind = len(set(nums))
    
    if selectNum < kind:
        return selectNum
    else:
        return kind