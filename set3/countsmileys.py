def count_smileys(arr):
    valid_eyes = ':;'
    valid_nose = '-~'
    valid_mouth = ')D'
    counter = 0
    for i in arr:
        if len(i) == 2:
            if i[0] in valid_eyes and i[-1] in valid_mouth:
                counter += 1
        elif len(i) == 3:
            if i[0] in valid_eyes and i[-1] in valid_mouth and i[-2] in valid_nose:
                counter += 1
        else:
            continue
    return counter


print(count_smileys([':D', ':~)', ';~D', ':)']))
