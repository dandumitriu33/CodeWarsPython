def to_camel_case(text):
    if text == '':
        return ''
    list_signs = list('-_')
    word_list = list(text)
    i = 0
    while i < len(word_list):
        if str(word_list[i]) in list_signs:
            word_list[i+1] = word_list[i+1].capitalize()
            word_list.remove(word_list[i])
        i += 1
    return ''.join(word_list)



print(to_camel_case("the-stealth-warrior"))
print(to_camel_case('The_Stealth_Warrior'))
print(to_camel_case('A-B-C'))
print(to_camel_case('the_cat_is_Omoshiroi'))