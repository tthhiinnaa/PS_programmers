from collections import deque
def solution(food):
    answer = ''
    dq = deque()
    dq.append(0)
    food2 = []
    for i in range(len(food)):
        food2.append(food[i]//2)
    print(food2)
    for i in range(len(food2)-1,-1,-1):
        for j in range((food2[i])):
            dq.append(i)
            dq.appendleft(i)
    print(dq)
    print(str(dq))
    answer = ''.join(map(str, dq))
    print(answer)
    return answer