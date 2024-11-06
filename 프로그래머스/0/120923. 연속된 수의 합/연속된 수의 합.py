def solution(num, total):
    answer = []
    addnum = int((total-sum(range(num+1)))/num)
    print(addnum)
    temp = range(addnum+1,num+addnum+1)
    answer = list(temp)
    print(answer)
    return answer