def delete_nth(order, max_e):
    unduplicated = []
    for i in order:
        if unduplicated.count(i) < max_e:
            unduplicated.append(i)
    return unduplicated


print(delete_nth([1, 1, 1, 1, 2, 2, 2, 3, 3, 3], 2))
