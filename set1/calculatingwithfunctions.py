def zero(calculate=None):
    if calculate is None:
        return 0
    elif calculate[0] == '+':
        result = 0 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 0 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 0 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 0 // int(calculate[1])
        return result


def one(calculate=None):
    if calculate is None:
        return 1
    elif calculate[0] == '+':
        result = 1 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 1 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 1 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 1 // int(calculate[1])
        return result


def two(calculate=None):
    if calculate is None:
        return 2
    elif calculate[0] == '+':
        result = 2 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 2 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 2 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 2 // int(calculate[1])
        return result


def three(calculate=None):
    if calculate is None:
        return 3
    elif calculate[0] == '+':
        result = 3 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 3 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 3 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 3 // int(calculate[1])
        return result


def four(calculate=None):
    if calculate is None:
        return 4
    elif calculate[0] == '+':
        result = 4 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 4 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 4 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 4 // int(calculate[1])
        return result


def five(calculate=None):
    if calculate is None:
        return 5
    elif calculate[0] == '+':
        result = 5 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 5 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 5 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 5 // int(calculate[1])
        return result


def six(calculate=None):
    if calculate is None:
        return 6
    elif calculate[0] == '+':
        result = 6 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 6 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 6 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 6 // int(calculate[1])
        return result


def seven(calculate=None):
    if calculate is None:
        return 7
    elif calculate[0] == '+':
        result = 7 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 7 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 7 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 7 // int(calculate[1])
        return result


def eight(calculate=None):
    if calculate is None:
        return 8
    elif calculate[0] == '+':
        result = 8 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 8 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 8 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 8 // int(calculate[1])
        return result


def nine(calculate=None):
    if calculate is None:
        return 9
    elif calculate[0] == '+':
        result = 9 + int(calculate[1])
        return result
    elif calculate[0] == '*':
        result = 9 * int(calculate[1])
        return result
    elif calculate[0] == '-':
        result = 9 - int(calculate[1])
        return result
    elif calculate[0] == '/':
        result = 9 // int(calculate[1])
        return result


def plus(number):
    operation = '+' + str(number)
    return operation


def minus(number):
    operation = '-' + str(number)
    return operation


def times(number):
    operation = '*' + str(number)
    return operation


def divided_by(number):
    operation = '/' + str(number)
    return operation


print(seven(plus(seven())))
