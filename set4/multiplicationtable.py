def multiplication_table(row, col):
    table = []
    for i in range(1, row+1):
        row = [x*i for x in range(1, col+1)]
        table.append(row)
    return table


print(multiplication_table(3, 2))
