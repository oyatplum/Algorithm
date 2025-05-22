answer = 0
def dfs(numbers, target, total, index):
    global answer
    if len(numbers) == index:
        if total == target:
            answer += 1
        return
    else:
        dfs(numbers, target, total + numbers[index], index+1)
        dfs(numbers, target, total - numbers[index], index+1)
    
def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer