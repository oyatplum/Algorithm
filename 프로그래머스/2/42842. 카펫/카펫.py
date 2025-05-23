def solution(brown, yellow):
    answer = []
    total = brown + yellow
    temp = []
    
    for i in range(1, total+1):
        if total % i == 0:
            temp.append(i)
        else:
            continue
    
    for row in temp:
        col = total // row
        if (row - 2) * (col - 2) == yellow:
            answer.append(row)
            answer.append(col)
            break
    answer.sort(reverse = True)
    return answer