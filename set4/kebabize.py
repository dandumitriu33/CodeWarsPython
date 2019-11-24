def kebabize(string):
    full_digits = True
    for i in string:
        if i.isdigit():
            full_digits = True
        else:
            full_digits = False
            break
    if full_digits is True:
        return ''
    for i in string:
        if i.isdigit():
            string = string.replace(i, '')
    for i in string:
        if i.isupper():
            string = string.replace(i, '-' + i.lower())
    for i in string:
        if i.isupper():
            string = string.replace(i, i.lower())
    if string[0] == '-':
        string = string[1:]
    return string


print(kebabize('-camelsHave3Humps'))
print(kebabize('8ZrEb05YRQM71Gr8wOlWsSWX'))
