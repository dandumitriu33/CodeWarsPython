def square_digits(num):
    num_list = [int(i)**2 for i in str(num)]
    return int(''.join([str(i) for i in num_list]))


print(square_digits(9119))
