def find_nb(m):
    sum_total = 0
    n = 1
    while sum_total < m:
        sum_total = sum_total + n**3
        n += 1
    if m - sum_total != 0:
        return -1
    else:
        return n-1


print(find_nb(4183059834009))
