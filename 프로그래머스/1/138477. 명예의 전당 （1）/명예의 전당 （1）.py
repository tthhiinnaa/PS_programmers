def solution(k, score):
    answer = []
    kwin = []
    for i in score:
        if len(kwin) < k:
            kwin.append(i)
        else:
            if min(kwin) < i:
                kwin.remove(min(kwin))
                kwin.append(i)
        answer.append(min(kwin))
    return answer