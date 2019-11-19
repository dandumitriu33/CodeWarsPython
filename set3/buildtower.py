def tower_builder(n_floors):
    tower_width = n_floors * 2 - 1
    tower_list = []
    n = '*'
    tower_list.append(n.center(tower_width, ' '))
    for i in range(2, n_floors+1):
        n = str((i * 2 - 1) * '*')
        tower_list.append(n.center(tower_width, ' '))
    return tower_list


print(tower_builder(4))
