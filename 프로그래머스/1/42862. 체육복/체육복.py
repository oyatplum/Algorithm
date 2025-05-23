def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+1)
    
    realLost = []
    realReserve = []
    
    for i in lost:
        if i not in reserve:
            realLost.append(i)
    for i in reserve:
        if i not in lost:
            realReserve.append(i)
            
    
    for i in realLost:
        students[i] = 0
    for i in realReserve:
        students[i] = 2
    del students[0]
    
    for idx, student in enumerate(students):
        if student == 0:
            if idx == 0: #처음
                if students[1] == 2: #뒤에서 빌림
                    students[1] = 1
                    students[0] = 1
            elif idx == len(students) - 1: #마지막
                if students[len(students) - 2] == 2: #앞에서 빌림
                    students[len(students) - 1] = 1
                    students[len(students) - 2] = 1
            else:
                if students[idx-1] == 2:
                    students[idx-1] = 1
                    students[idx] = 1
                elif students[idx+1] == 2:
                    students[idx+1] = 1
                    students[idx] = 1
            
    for i in students:
        if i > 0:
            answer += 1
    
    return answer