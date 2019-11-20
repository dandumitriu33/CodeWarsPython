def expand_number(n):
    div = 10
    remainder = 0
    result_list = []
    for i in range(len(str(n))):
        remainder = n % div
        if remainder != 0:
            result_list.insert(0, str(remainder))
        n = n - remainder
        div *= 10
    return ' + '.join(result_list)


print(expand_number(70304))
