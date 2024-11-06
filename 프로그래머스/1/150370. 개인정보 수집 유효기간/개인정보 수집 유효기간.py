from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    today_list = list(map(int,(today.split("."))))
    print(today_list)
    today_num = today_list[0]*12*28+today_list[1]*28+today_list[2]
    print(today_num)
    dicts = defaultdict(list)
    for i in terms:
        A,B= i.split(" ")
        dicts[A].append(int(B)*28)
    #print(int(dicts.get("A")))
    #print(type(dicts.get("B")))
    for i, j in enumerate(privacies):
        A,K=j.split(" ")
        print(type(K))
        past_list = list(map(int, (A.split("."))))
        past_num = past_list[0] * 12 * 28 + past_list[1] * 28 + past_list[2]
        print(K)
        #print(dicts[K])
        if today_num - past_num >= int(dicts.get(K)[0]):
            answer.append(i+1)
    print(dicts)
    print(answer)
    return answer
