def xo(s):
    os = 0
    xs = 0
    for i in s:
        if i == 'o' or i == 'O':
            os += 1
        elif i == 'x' or i == 'X':
            xs += 1
        else:
            continue
    if os == xs:
        return True
    else:
        return False


print(not xo('xxxoo'))
