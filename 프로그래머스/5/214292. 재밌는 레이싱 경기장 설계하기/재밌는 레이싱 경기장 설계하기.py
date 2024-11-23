from collections import defaultdict
import math


def solution(heights):
    answer = 1
    heights_dict = defaultdict(int)
    for h in heights:
        heights_dict[h] += 1
    heights_dicts = dict(heights_dict)
    #print(heights_dicts)


    #print(len(heights))
    #print(type(heights))
    heights = sorted(heights)
    #print(heights)
    temp = 0
    for key,value in heights_dicts.items():
        if value > math.ceil(len(heights)/2) :
            return 0
        # else:
    len_H =len(heights)
    temp_even = 1000000000
    temp_even2 = 1000000000
    if len_H%2 == 0:
        for i in range(len_H//2):
            half_temp = heights[i+len_H//2]-heights[i]
            #print(half_temp)
            if temp_even > half_temp:
                temp_even = half_temp
        return temp_even
    # else:
    #     for i in range(len_H // 2+1):
    #         half_temp = heights[i + len_H // 2] - heights[i]
    #
    #         #print(half_temp)
    #         if temp_even > half_temp:
    #             temp_even = half_temp
    #
    #         min(heights[1]-heights[0],heights[-1])
    #     for i in range(len_H // 2):
    #         half_temp = heights[i + len_H // 2+1] - heights[i]
    #         #print(half_temp)
    #         if temp_even2 > half_temp:
    #             temp_even2 = half_temp
    #     answer = min(temp_even,temp_even2)
    else:
        for i in range(len_H // 2 ):
            half_temp = heights[i + len_H // 2] - heights[i]

            # print(half_temp)
            if temp_even > half_temp:
                temp_even = half_temp
        temp_even = min(heights[1]-heights[0],temp_even)

        for i in range(len_H // 2):
            half_temp = heights[i + len_H // 2 + 1] - heights[i+1]
            # print(half_temp)
            if temp_even2 > half_temp:
                temp_even2 = half_temp
        temp_even2 = min(temp_even2,heights[-1]-heights[-2])
        temp_even3 = min(heights[len_H//2+1]-heights[0],heights[-1]-heights[len_H//2+1])
        answer = max(temp_even,temp_even2,temp_even3)
        empty_list = [heights[-1]]
        for i in range(len_H//2):
            empty_list.append(heights[len_H//2+i])
            empty_list.append(heights[i])

        min_even = []
        for i in range(len(heights)-1):
            min_even.append(abs(empty_list[i+1]-empty_list[i]))


        smallest = min(min_even)
        #print(min_even)
        smallest_i = min_even.index(smallest)
        min_even.remove(smallest)
        #print(min(min_even))
        answer = min(min_even)
    return answer