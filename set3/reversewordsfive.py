def spin_words(sentence):
    word_list = sentence.split()
    result_list = []
    for i in word_list:
        if len(i) >= 5:
            result_list.append(i[::-1])
        else:
            result_list.append(i)
    return ' '.join(result_list)


print(spin_words("Hey fellow warriors"))
