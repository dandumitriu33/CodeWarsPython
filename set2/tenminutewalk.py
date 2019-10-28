def take_a_walk(walk):
    dict_coords = {
        'n': [0, 1],
        's': [0, -1],
        'w': [-1, 0],
        'e': [1, 0]
    }
    start = [0, 0]
    result = [0, 0]
    for j in walk:
        result = [result[k] + dict_coords[j][k] for k in [0, 1]]
    if len(walk) > 10 or len(walk) < 10:
        return False
    if result == start:
        return True
    else:
        return False


print(take_a_walk(['n', 's', 'w', 'e', 'e']))
