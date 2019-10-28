def dig_pow(n, p):
    length_n = len(str(n))
    n = str(n)
    list_n = list(n)
    numero_uno = 0
    for i in list_n:
        numero_uno = numero_uno + int(i)**p
        p += 1
    if numero_uno % int(n) == 0:
        return int(numero_uno / int(n))
    else:
        return -1


print(dig_pow(46288, 3))
