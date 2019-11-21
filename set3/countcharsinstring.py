def count(string):
    string_dictionary = {}
    for i in string:
        string_dictionary[i] = string.count(i)
    return string_dictionary


print(count('aba'))
