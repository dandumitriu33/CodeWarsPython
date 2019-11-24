import re


def is_valid_phone_number(string):
    PHONE_NUMBER_LENGTH = 14
    if len(string) != 14:
        return False
    if re.search(r"[(][0-9][0-9][0-9][)][ ][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]", string):
        return True
    else:
        return False


print(is_valid_phone_number("(123) 456-7890"))
