def remove_smallest(numbers):
    if numbers != []:
        smallest = min(numbers)
        i = numbers.index(smallest)
        non_boring_list = numbers[:]
        non_boring_list.remove(non_boring_list[i])
    else:
        non_boring_list = []
    return non_boring_list


print(remove_smallest([]))
