from collections import defaultdict
def solution(genres, plays):
    answer = []
    d1 = defaultdict(int)
    #{'classic': 1450, 'pop': 3100})
    d2 = defaultdict(list)
    #{'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]})
    
    for i, (j,k) in enumerate(zip(genres, plays)):
        d1[j] += k
        d2[j] += [(k,i)]
    
    for i,j in sorted(d1.items(), key=lambda x:x[1], reverse = True):
        for k,v in sorted(d2[i], key=lambda x:(-x[0], x[1]))[:2]:
            answer.append(v)
    return answer