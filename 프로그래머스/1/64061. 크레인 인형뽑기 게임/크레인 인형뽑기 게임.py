def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for line in board:
            if line[move-1] != 0:
                stack.append(line[move-1])
                line[move-1] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop(-1)
            stack.pop(-1)
    return answer