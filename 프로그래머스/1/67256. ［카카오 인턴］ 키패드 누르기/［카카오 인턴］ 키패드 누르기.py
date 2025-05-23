def solution(numbers, hand):
    answer = ''
    curLeft = '*'
    curRight = '#'
    dis = [[0,4,3,4,3,2,3,2,1,2],
           [4,0,1,2,1,2,3,2,3,4],
           [3,1,0,1,2,1,2,3,2,3],
           [4,2,1,0,3,2,1,4,3,2],
           [3,1,2,3,0,1,2,1,2,3],
           [2,2,1,2,1,0,1,2,1,2],
           [3,3,2,1,2,1,0,3,2,1],
           [2,2,3,4,1,2,3,0,1,2],
           [1,3,2,3,2,1,2,1,0,1],
           [2,4,3,2,3,2,1,2,1,0],
           [1,3,4,5,2,3,4,1,2,3], # '*'
           [1,5,4,3,4,3,2,3,2,1]] # '#'
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            curLeft = num
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            curRight = num
            answer += 'R'
        else: #2, 5, 8, 0인 경우
            if curLeft == '*':
                disLeft = dis[10][num]
            elif curLeft == '#':
                disLeft = dis[11][num]
            else:
                disLeft = dis[curLeft][num]
            
            if curRight == '*':
                disRight = dis[10][num]
            elif curRight == '#':
                disRight = dis[11][num]
            else:
                disRight = dis[curRight][num]
            
            if disLeft < disRight:
                curLeft = num
                answer += 'L'
            elif disLeft > disRight:
                curRight = num
                answer += 'R'
            else: #거리 같은 경우
                if hand == "left":
                    curLeft = num
                    answer += 'L'
                else:
                    curRight = num
                    answer += 'R'
            
    return answer