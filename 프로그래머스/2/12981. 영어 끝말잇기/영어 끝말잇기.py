

def solution(n, words):
    answer = [0,0]
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
        #if words[i][0] != words[i-1][-1] or len(set(words[:i+1])) != len(words[:i+1]):\
            return [i%n+1,i//n+1]
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer