def check(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6
    
def solution(lottos, win_nums):
    answer = []
    win = 0
    zero = 0
    lose = 0
    for l in lottos:
        if l == 0:
            zero += 1
        if l in win_nums:
            win += 1
            
    lose = len(lottos) - (win+zero)
    
    best = check(win + zero)
    worst = check(len(lottos) - (lose + zero))
    answer.append(best)
    answer.append(worst)   
    return answer