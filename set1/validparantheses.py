def valid_parentheses(string):
    if first_para(string) is False:
        return False
    if last_para(string) is False:
        return False
    if parse_string(string) is False:
        return False
    else:
        return True


def first_para(string):
    i = 0
    first_para = ''
    while i < len(string):
        if string[i] == '(' or string[i] == ')':
            first_para = string[i]
            break
        else:
            i += 1
            continue
    if first_para == ')':
        return False
    elif first_para == '':
        return True
    else:
        return True


def last_para(string):
    j = len(string) - 1
    last_para = ''
    while j >= 0:
        if string[j] == ')' or string[j] == '(':
            last_para = string[j]
            break
        else:
            j -= 1
            continue
    if last_para == '(':
        return False
    else:
        return True


def parse_string(string):
    i = 0
    open_para = 0
    while i < len(string):
        if string[i] == '(':
            open_para += 1
            i += 1
        elif string[i] == ')':
            i += 1
            open_para -= 1
            if open_para == -1:
                break
                return False
        else:
            i += 1
            continue
    if open_para != 0:
        return False
    else:
        return True


print(valid_parentheses("f(jc)l)bnqh(pvy()(m)g()d"))
