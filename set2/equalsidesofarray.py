def equal_sides(arr):
    for i in range(len(arr)):
        head = arr[:i]
        tail = arr[i+1:]
        if sum(head) == sum(tail):
            return i
    return -1


print(equal_sides([0, -28, 9, 0, -29, -10, 0]))
