def solution(s):
    dic = dict()

    result = []
    for idx, w in enumerate(s):
        if w not in dic:
            result.append(-1)
        else:
            result.append(idx - dic[w])
        dic[w] = idx
    return result