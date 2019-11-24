import re


def is_valid_phone_number(string):
    if re.match(r"[(][0-9][0-9][0-9][)][ ][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]", string):
        return True
    return False


print(is_valid_phone_number("(123) 456-7890"))
