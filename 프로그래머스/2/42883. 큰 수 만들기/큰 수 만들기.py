def solution(number, k):
    answer = ''
    
    q = []
    q.append(int(number[0]))
    cur = int(number[0])
    count = 0
    
    for num in number[1:]:
        if cur < int(num):
            cur = int(num)
            while q and count < k and q[-1] < int(num):
                q.pop()
                count += 1
            q.append(int(num))
        else:
            cur = int(num)
            q.append(int(num))
    
    lenQ = len(number) - k
    
    for i in q[:lenQ]:
        answer += str(i)
        
    return answer