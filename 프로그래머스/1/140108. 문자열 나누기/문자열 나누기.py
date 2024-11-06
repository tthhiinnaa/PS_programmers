def solution(s):
    answer = 0
    x = s[0]
    cnt_same = 0
    cnt_diff = 0
    for i in range(len(s)-1):
        if x == s[i]:
            cnt_same += 1
        else:
            cnt_diff += 1
        
        if cnt_same == cnt_diff:
            answer += 1
            x = s[i+1]
        
        
    return answer + 1
