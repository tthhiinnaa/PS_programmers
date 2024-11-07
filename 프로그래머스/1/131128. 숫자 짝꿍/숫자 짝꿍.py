from collections import Counter

def solution(X,Y):

    dictX = dict(Counter(X))
    dictY = dict(Counter(Y))
    dictA = {}
    for keyX, valueX in dictX.items():
        for keyY, valueY in dictY.items():
            if keyX == keyY:
                dictA[keyX] = min(valueX,valueY)
    sorted_dict = sorted(dictA.items(), key=lambda item: item[0], reverse=True)
    if len(sorted_dict) == 0:
        return "-1"
    if sorted_dict[0][0] == "0":
        return "0"
    answer = []
    for i in range(len(sorted_dict)):
        for j in range(sorted_dict[i][1]):
            answer.append(sorted_dict[i][0])
    answerSTR = "".join(answer)
    return answerSTR