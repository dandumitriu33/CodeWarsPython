def prefill(n, v=None):
    if type(n) == str and not n.isdigit():
        return f'{n} is invalid'
    if type(n) == float:
        return f'{n} is invalid'
    if n is None:
        return f'None is invalid'
    if type(n) == str:
        n = int(n)
    result = []
    result.append(v)
    result = result * n
    return result


print(prefill('1', 1))
