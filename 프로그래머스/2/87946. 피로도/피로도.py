from itertools import permutations

def solution(k, dungeons):
    answer = 0
    temp = list(permutations(dungeons, len(dungeons)))
    
    for dungeon in temp:
        posK = k
        total = 0
        for d in dungeon:
            if posK >= d[0]: #던전 참여 가능
                posK -= d[1]
                total += 1
        if answer < total:
            answer = total
    
    return answer