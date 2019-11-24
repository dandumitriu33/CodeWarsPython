import math


def is_square(number):
    if number >= 0 and math.sqrt(number) % 1 == 0:
        return True
    return False


print(is_square(25))
