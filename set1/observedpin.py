from itertools import permutations, combinations


def get_pins(observed):
    list_of_possibles = []
    keypress = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }
    # print(keypress)  # remove after
    pre_result = []
    result = []
    if len(observed) == 1:
        result = keypress[observed]
    elif len(observed) != 1:
        list_of_possibles = []
        for i in observed:
            list_of_possibles.append(keypress[i])
        # print(list_of_possibles)
    momo = len(observed)
    final_list_result = []
    omg_result = []
    while momo > 1:
        pre_result = combinations(list_of_possibles[-momo] + list_of_possibles[-momo + 1], 2)
        momo -= 1
        print(pre_result)
        list_of_possibles.pop()
        print(list_of_possibles)
        set_result = set(pre_result)
        print(set_result)
        list_result = list(set_result)
        print(list_result)
        for i in list_result:
            item = i[0] + i[1]
            final_list_result.append(item)
        list_of_possibles[-1] = final_list_result
    omg_result = final_list_result
    
    for u in omg_result:
        if len(u) == len(observed):
            result.append(u)

    # pre_result = combinations(list_of_possibles, len(observed))
    # # print(pre_result)
    # m = list(pre_result)
    # for j in m:
    #     if j[0] in keypress[observed[0]]:
    #         unit = j
    #         final_unit = ''
    #         for q in unit:
    #             final_unit = final_unit + q
    #         result.append(final_unit)
    # # print(result)
    # set_result = set(result)
    # # print(set_result)
    # list_result = list(set_result) 
    result.sort()
    return result
       

print(get_pins('369'))









# list_of_possibles = []
#     final_list = []
#     for i in observed:
#         list_of_possibles.append(keypress[i])
#     print(list_of_possibles)
    
#     for j in list_of_possibles[0]:
#         for k in list_of_possibles[1]:
#             result = j + k
#             final_list.append(result)
#     mmm = final_list[:]
#     print(mmm)









# num_of_keys = len(observed)
#     print(num_of_keys)
#     n = -(num_of_keys - 1)
#     print(n)
#     puppet_list = []
#     while n < 0:
#         for i in list_of_possibles[n+1]:
#             for j in list_of_possibles[n]:
#                 puppet = i + j
#                 puppet_list.append(puppet)
#         list_of_possibles[n+1] = puppet_list
#         n += 1
#     print(puppet_list)
#     return puppet_list
