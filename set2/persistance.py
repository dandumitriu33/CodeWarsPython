def persistence(number):
    n = str(number)
    length_of_number = len(n)
    persistence_counter = 0
    while length_of_number > 1:
        new_n = 1
        for i in str(n):
            new_n = new_n * int(i)
        persistence_counter += 1
        n = new_n
        length_of_number = len(str(n))
    return persistence_counter



print(persistence(39))