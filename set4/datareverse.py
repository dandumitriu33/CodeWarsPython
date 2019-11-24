def data_reverse(data):
    list_of_numbers = []
    item_list = []
    while len(data) > 0:
        item_list = [i for i in data[:8]]
        j = len(item_list) - 1
        while j >= 0:
            list_of_numbers.insert(0, item_list[j])
            j -= 1
        for i in range(0, 8):
            data.pop(0)
    return list_of_numbers


print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))
