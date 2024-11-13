def solution(x):
    answer = []
    
    cnt = 0
    zero = 0
    
    while x != '1':
        cnt += 1
        one = x.count("1")
        zero += len(x)-one
        x= bin(one)[2:]
    
    return [cnt,zero]