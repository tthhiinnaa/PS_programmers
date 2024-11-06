import string


def solution(s, skip, index):
    answer = ''
    alps = list(string.ascii_lowercase)
    skip_list = list(skip)
    for i,k in enumerate(skip_list):
        if k in alps:
            alps.remove(k)
    print(alps)

    for j in s:
        for k in range(len(alps)):
            if j == alps[k]:
                answer += alps[(k+index)%len(alps)]

    print(answer)
    return answer