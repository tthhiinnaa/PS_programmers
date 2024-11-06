def solution(dots):
    answer = 0
    #1, 2 번 연결
    ans1 = (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
    #3,4번연결
    ans2 = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
    #1번 3번연결
    ans3 = (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
    #2,4번 연결
    ans4 = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])
    #1, 4 번 연결
    ans5 = (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
    #2,3번연결
    ans6 = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
    if ans1 == ans2 or ans3 == ans4 or ans5 == ans6:
        return 1
    return 0