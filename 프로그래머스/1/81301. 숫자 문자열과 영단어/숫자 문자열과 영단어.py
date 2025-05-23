def solution(s):
    answer = ''
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight', 'nine']
    
    temp = []
    
    string = ''
    for i in s:
        if i.isdigit():
            temp.append(i)
            continue
        else:
            string += i
            if string in words:
                temp.append(words.index(string))
                string = ''
    
    for i in temp:
        answer += str(i)
    return int(answer)