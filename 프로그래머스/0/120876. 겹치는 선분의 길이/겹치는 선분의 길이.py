def solution(lines):
    answer = 0
    A = list(range(lines[0][0],lines[0][1]))
    B = list(range(lines[1][0],lines[1][1]))
    C = list(range(lines[2][0],lines[2][1]))
    print(A,B,C)
    answer = len((set(A)&set(B))|(set(B)&set(C))|(set(C)&set(A)))
    return answer