# def solution(keymap, targets):
#     answer = []
#     dicts = {}
#     for keys in keymap:
#         for i,j in enumerate(keys):
#             if j not in dicts.keys():
#                 dicts[j] = i
#             else:
#                 if dicts[j] > i:
#                     dicts[j] = i
#     for i in dicts:
#         dicts[i] += 1
#     for target in targets:
#         answer_o = 0
#         for s in target:
#             if s not in dicts.keys():
#                 return [-1]
#             answer_o += dicts[s]
#         answer.append(answer_o)

#     return answer

# def solution(keymap, targets):
#     # 각 문자가 최소 몇 번 눌러야 하는지 저장할 딕셔너리
#     key_press_count = {}
    
#     # keymap에서 각 문자에 대해 최소 키 입력 횟수를 계산
#     for keys in keymap:
#         for i, char in enumerate(keys):
#             if char not in key_press_count:
#                 key_press_count[char] = i + 1
#             else:
#                 key_press_count[char] = min(key_press_count[char], i + 1)
    
#     # 각 target에 대해 최소 키 입력 횟수를 계산
#     result = []
#     for target in targets:
#         total_presses = 0
#         for char in target:
#             # 문자가 keymap에 없으면 작성할 수 없으므로 -1 리턴
#             if char not in key_press_count:
#                 total_presses = -1
#                 break
#             total_presses += key_press_count[char]
        
#         result.append(total_presses)
    
#     return result

def solution(keymap,targets):
    key_press_count = {} # 최소 알파벳의 입력 숫자
    
    # keymap에서 각 문자에 대해 최소 키 입력 횟수를 계산
    for keys in keymap:
        for i, char in enumerate(keys):
            if char not in key_press_count:
                key_press_count[char] = i + 1
            else:
                key_press_count[char] = min(key_press_count[char], i + 1)
    result = []
    print(key_press_count)
    for target in targets:
        result_sum = 0
        for a in target:
            if not a in key_press_count:
                result_sum = -1
                break
            else:
                result_sum += key_press_count[a]
        result.append(result_sum)
    return result
    
    
    