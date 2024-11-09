def solution(s):
    answer = []
    while s:
        if s[0].isdigit():
            answer.append(s[0])
            s = s[1:]
        elif s[0] == 'z':
            answer.append(0)
            s = s[4:]
        elif s[0] == 'o':
            answer.append(1)
            s = s[3:]
        elif s[0] == 't':
            s = s[1:]
            if s[0] == 'w':
                answer.append(2)
                s = s[2:]
            elif s[0] == 'h':
                answer.append(3)
                s = s[4:]
        elif s[0] == 'f':
            s = s[1:]
            if s[0] == 'o':
                answer.append(4)
                s = s[3:]
            elif s[0] == 'i':
                answer.append(5)
                s = s[3:]
        elif s[0] == 's':
            s = s[1:]
            if s[0] == 'i':
                answer.append(6)
                s = s[2:]
            elif s[0] == 'e':
                answer.append(7)
                s = s[4:]

        elif s[0] == 'e':
            answer.append(8)
            s = s[5:]
        elif s[0] == 'n':
            answer.append(9)
            s = s[4:]
        elif len(s) ==0:
            break
    answer = ''.join(str(i) for i in answer)
    answer = int(answer)
    return answer
