count = 0
flag = False
answer = 0
def dfs(start, word, alpha, string):
    global count, answer
    
    if string == word:
        flag = True
        answer = count
        return
    
    if len(string) == 5:
        return
    
    string += start
    count += 1
    
    for a in alpha:
        dfs(a, word, alpha, string)

def solution(word):
    global answer
    alpha = ['A', 'E', 'I', 'O', 'U']
    string = ''
    
    for a in alpha:
        dfs(a, word, alpha, string)
        if flag:
            break
    return answer