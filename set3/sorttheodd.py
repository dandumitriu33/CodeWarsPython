def sort_array(source_array):
    if source_array == []:
        return []
    swap = True
    while swap is True:
        swap = False
        i = 0
        while i < len(source_array):
            if source_array[i] % 2 == 1:
                j = i + 1
                while j < len(source_array):
                    if source_array[j] % 2 == 1:
                        if source_array[i] > source_array[j]:
                            temp = source_array[i]
                            source_array[i] = source_array[j]
                            source_array[j] = temp
                            swap = True
                    j += 1
            i += 1
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))
