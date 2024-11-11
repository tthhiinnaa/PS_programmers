def solution(s):
    answer = True
    pnum = 0
    ynum = 0
    for count in s:
        if count == "p" or count == "P" :
            pnum+=1
        if count == "y" or count =="Y":
            ynum+=1
    if pnum == ynum : 
        return True
    else:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.