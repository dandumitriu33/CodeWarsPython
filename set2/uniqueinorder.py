def unique_in_order(word):
    if word == [] or word == '':
        return []
    result = []
    result.append(word[0])
    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            result.append(word[i])
    return result


print(unique_in_order([1,2,2,3,3]))
