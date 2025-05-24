def solution(answers):
    answer = []
    first = [1,2,3,4,5] #5
    second = [2,1,2,3,2,4,2,5] #8
    third = [3,3,1,1,2,2,4,4,5,5] #10
    temp = [0,0,0]
    
    for idx, a in enumerate(answers):
        if a == first[idx%5]:
            temp[0] += 1
        if a == second[idx%8]:
            temp[1] += 1
        if a == third[idx%10]:
            temp[2] += 1
            
    maxNum = max(temp)
    
    for idx, t in enumerate(temp):
        if t == maxNum:
            answer.append(idx+1)

    return answer