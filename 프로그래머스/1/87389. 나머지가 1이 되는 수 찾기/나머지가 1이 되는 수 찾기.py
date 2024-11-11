def solution(n):
    answer = 2
    for answer in range(answer,n):
        if (n-1)%answer==0:
            return answer
    