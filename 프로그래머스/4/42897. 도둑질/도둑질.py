def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n
    
    #첫번째 집 터는 경우
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    #첫번째 집 안 터는 경우
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(max(dp1), max(dp2))