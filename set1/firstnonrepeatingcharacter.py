def first_non_repeating_letter(string):
    lowered_string = string.lower()
    print(lowered_string)
    for letter in string:
        if lowered_string.count(letter.lower()) == 1:
            return letter
            break
        elif lowered_string.count(letter.lower()) != 1:
            continue
    return ""


print(first_non_repeating_letter('Azaab'))
