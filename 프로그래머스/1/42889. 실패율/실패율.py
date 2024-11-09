from collections import Counter

def solution(N, stages):
    s = Counter(stages) # 스테이지 별 Count
    print(s)
    challengers = len(stages) 
    rate = {k:0 for k in range(1, N + 1)}

    for stage in range(1, N + 1):
        if challengers != 0:
            rate[stage] = s[stage] / challengers
            challengers -= s[stage]
        else:
            rate[stage] = 0

    answer = dict(sorted(rate.items(), key= lambda x: x[1], reverse=True))
    answers = []
    for key in answer.keys():
        answers.append(key)
    return answers