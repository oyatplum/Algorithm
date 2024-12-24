def solution(n):
    t = 1
    x = -1
    y = 0
    output = []
    matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            
            matrix[x][y] = t
            t += 1
            
    for i in matrix:
        for j in i:
            if j != 0:
                output.append(j)
                
    return output