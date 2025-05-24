def solution(numbers):
    answer = ''
    strNum = list(map(str, numbers))
    strNum.sort(key = lambda x:x*3, reverse = True)
    for i in strNum:
        answer += i
    return str(int(answer))