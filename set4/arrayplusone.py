def plus_one(arr):
    if arr == []:
        return None
    string = ''
    for i in arr:
        if i < 0:
            return None
        string += str(i)
    result = str(int(string) + 1)
    result_list = []
    for i in result:
        result_list.append(int(i))
    return result_list


print(plus_one([2, 3, 9]))
