def split_strings(word):
    word_list = list(word)
    result = []
    if len(word_list) % 2 == 1:
        word_list.append('_')
    i = 0
    while i < len(word_list):
        temp = word_list[i] + word_list[i+1]
        result.append(temp)
        i += 2
    return result


print(split_strings('abcdefj'))