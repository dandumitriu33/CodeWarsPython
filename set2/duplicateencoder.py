def duplicate_encoder(text):
    result = []
    g = text.lower()
    for i in g:
        if g.count(str(i)) == 1:
            result.append('(')
        elif g.count(str(i)) > 1:
            result.append(')')
    print(result)
    return ''.join(result)


print(duplicate_encoder('(( @'))
