def solution(lottos, win_nums):
    answer = []
    countL = lottos.count(0)
    if countL == 6:
        return 1,6
    setL = set(lottos)
    setW = set(win_nums)
    countW = len(setL & setW)
    if countW == 0:
        return 6-countL, 6
    answer = 6-countW-countL+1, 6-countW+1
    return answer