def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    list_of_numbers = []
    for i in range(a, b+1):
        if eureka(i):
            list_of_numbers.append(i)
    list_of_numbers.sort()
    return list_of_numbers


def eureka(number):
    sum_of_digits = 0
    i = 0
    number = str(number)
    while i < len(number):
        sum_of_digits = sum_of_digits + int(number[i])**(i+1)
        i += 1
    if int(number) == sum_of_digits:
        return True


print(sum_dig_pow(90, 100))
