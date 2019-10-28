def order_weight(strng):
    list_of_real = strng.split()
    list_of_false = []
    list_of_pairs = []
    wall_list = []
    for weight in list_of_real:
        false_weight = 0
        for digit in weight:
            false_weight = false_weight + int(digit)
        list_of_false.append(false_weight)        
    print(list_of_real)
    print(list_of_false)
    element = []
    for i in range(0, len(list_of_real)):
        element.append(list_of_false[i])
        element.append(list_of_real[i])
        list_of_pairs.append(element)
        element = []
    print(list_of_pairs)
    list_of_pairs.sort()
    print(list_of_pairs)
    for j in range(0, len(list_of_pairs)):
        wall_list.append(list_of_pairs[j][1])
    print(wall_list)
    result = ' '.join(wall_list)
    return result

    
print(order_weight('2000 10003 1234000 44444444 9999 11 11 22 123'))






# list_of_weights = strng.split()
#     list_of_weights.sort()
#     print(list_of_weights)
#     list_of_false_weights = []
#     for weight in list_of_weights:
#         false_weight = 0
#         for digit in weight:
#             false_weight = false_weight + int(digit)
#         list_of_false_weights.append(false_weight)
#     list_of_false_weights.sort()
#     list_of_false_weights = list(map(str, list_of_false_weights))
#     result = ' '.join(list_of_false_weights)
#     return result


#     list_of_weights = strng.split()
#     for conv in range(0, len(list_of_weights)):
#         list_of_weights[conv] = int(list_of_weights[conv])
#     list_of_weights.sort()
#     for conv2 in range(0, len(list_of_weights)):
#         list_of_weights[conv2] = str(list_of_weights[conv2])
#     list_of_false_weights = []
#     correspondents = {}
#     wall_list = []
#     for weight in list_of_weights:
#         false_weight = 0
#         for digit in weight:
#             false_weight = false_weight + int(digit)
#         list_of_false_weights.append(false_weight)
#     print(list_of_weights, '\n', list_of_false_weights)
#     i = 0
#     while i < len(list_of_weights):
#         correspondents[list_of_weights[i]] = list_of_false_weights[i]
#         i += 1
#     print(correspondents)
#     list_of_false_weights.sort()
#     for j in list_of_false_weights:
#         for key in correspondents:
#             if correspondents[key] == j:
#                 wall_list.append(key)
#     wall_list = list(map(str, wall_list))
#     result = ' '.join(wall_list)
#     return result