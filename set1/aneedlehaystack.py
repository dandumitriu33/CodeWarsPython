def find_needle(haystack):
    result = haystack.index('needle')
    return f'found the needle at position {result}'


print(find_needle(['3', '123124234', None, 'needle']))
