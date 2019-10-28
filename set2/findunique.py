def find_uniq(arr):
    element_one = arr[0]
    element_two = arr[1]
    if element_one == element_two:
        gg = set(arr)
        gg.discard(element_one)
        result = list(gg)
        return result[0]
    elif element_one == arr[2]:
        return element_two
    elif element_two == arr[2]:
        return element_one







print(find_uniq([ 1, 1, 1, 1, 1, 1, 1, 2, 1, 1 ]))