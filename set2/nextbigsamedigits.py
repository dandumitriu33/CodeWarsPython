import itertools


def next_bigger(n):
    n = str(n)
    if len(n) >= 7:
        break_point = len(n) - len(n)//3
        if break_point > 7:
            break_point = 7
        a = n[:-break_point]
        b = n[-break_point:]
    else:
        a = ''
        b = n
    # print(a + b)
    permutations = list(itertools.permutations(b))
    # print(permutations)
    x = set(permutations)
    permutations = list(x)
    permutations.sort()
    print(permutations)
    g = permutations.index(tuple(b))
    permutations.append('e')
    if permutations == []:
        return -1
    elif permutations[g+1] == 'e':
        return -1
    else:
        return int(a + ''.join(permutations[g+1]))


print(next_bigger(144))



# working but too long for huge numbers

# import itertools


# def next_bigger(n):
#     n = str(n)
#     permutations = list(itertools.permutations(n))
#     g = permutations.index(tuple(n))
#     permutations.append('-1')
#     if permutations == []:
#         return -1
#     elif permutations[g] == permutations[g+1]:
#         g += 1
#         return int(''.join(permutations[g+1]))
#     else:
#         return int(''.join(permutations[g+1]))







    # print(permutations)
    # valid_list = []
    # for i in permutations:
    #     valid_number = ''.join(i)
    #     if int(valid_number) > int(n):
    #         return int(valid_number)
    # return -1
    #         valid_list.append(int(valid_number))
    # print(valid_list)
    # valid_list.sort()
    # print(valid_list)
    # if valid_list == []:
    #     return -1
    # else:
    #     return valid_list[0]

