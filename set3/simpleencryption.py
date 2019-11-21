def encrypt(text, n):
    if text is None:
        return None
    i = 0
    str_result = text
    while i < n:
        str_result = text[1::2] + text[::2]
        text = str_result
        i += 1
    return str_result


def decrypt(encrypted_text, n):
    if encrypted_text is None:
        return None
    encrypted_list = list(encrypted_text)
    i = 0
    result = encrypted_text
    while i < n:
        p2 = result[:len(result)//2]
        p1 = result[len(result)//2:]
        result = ''
        j = 0
        while j < len(encrypted_text)//2:
            result = result + p1[j] + p2[j]
            j += 1
        i += 1
        if len(p1) > len(p2):
            result = result + p1[-1]
        elif len(p2) > len(p1):
            result = result + p2[-1]
    return result


print(encrypt('This is a test!', 2))
print(decrypt("s eT ashi tist!", 2))
