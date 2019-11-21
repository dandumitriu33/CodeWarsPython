def wave(string):
    string_list = list(string)
    result = []
    for i in range(len(string_list)):
        string_list[i] = string_list[i].upper()
        if ''.join(string_list) != string:
            result.append(''.join(string_list))
        string_list[i] = string_list[i].lower()
    return result


print(wave('hello world'))
