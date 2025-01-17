def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    rocks.append(distance)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        dist = 0
        prev_rock = 0
        delete = 0
        
        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid:
                delete += 1
                if delete > n:
                    break
            else:
                prev_rock = rock
                
        if delete > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer