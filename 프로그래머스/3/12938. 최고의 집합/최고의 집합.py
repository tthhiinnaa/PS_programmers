def solution(n, s):
    answer = []
    if n > s:
        answer = [-1]
        return answer
    quotient = s // n
    remainder = s % n
    for i in range(n):
        answer.append(quotient)
    for i in range(remainder):
        answer[len(answer) - 1- i] += 1

    return answer