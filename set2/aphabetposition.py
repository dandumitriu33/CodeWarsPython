def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for i in text:
        i = i.lower()
        if i in alphabet:
            index = alphabet.find(i)
            result.append(str(index + 1))
        else:
            continue
    return ' '.join(result)

print(alphabet_position("The sunset sets at twelve o' clock."))