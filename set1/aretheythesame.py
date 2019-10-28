def comp(array1, array2):
    i = 0
    result = True
    if array1 == [] and array2 == []:
        result = True
    elif array1 == [] or array2 == []:
        result = False
    elif len(array1) != len(array2):
        result = False
    elif len(array1) == len(array2):
        while i < len(array1):
            if array1[i] * array1[i] in array2:
                result = True
                array2.remove(array1[i] * array1[i])
            else:
                result = False
                break
            i += 1
    else:
        result = False
    return result


print(comp([32, 95, 25, 95, 81, 24], [1024, 9026, 625, 9025, 6561, 576]))
