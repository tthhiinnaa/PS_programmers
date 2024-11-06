def solution(t, p):
    answer = 0
    pnum = len(p)
    for i in range(len(t)-pnum+1):
        if t[i:i+pnum]<=p:
            answer += 1
    return answer