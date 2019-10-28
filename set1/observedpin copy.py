def get_pins(observed):
    pin_length = len(observed)
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
    result = []
    list_of_possibles = []
    element = 0
    temp_list = []
    for i in observed:
        list_of_possibles.append(keypress[i])
        # print(list_of_possibles)
    while pin_length > 1:
        for i in list_of_possibles[-2]:
            for j in list_of_possibles[-1]:
                element = i + j
                temp_list.append(element)
        # print(temp_list)
        list_of_possibles.pop()
        list_of_possibles[-1] = temp_list
        temp_list = []
        pin_length -= 1
    # print(list_of_possibles)
    result = list_of_possibles[0]
    return result


print(get_pins('369'))