def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = s.lower()
    for i in alphabet:
        if i not in text:
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))