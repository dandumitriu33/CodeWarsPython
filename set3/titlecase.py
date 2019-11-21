def title_case(title, minor_words):
    if title == '':
        return ''
    if minor_words is None:
        return title.title()
    minor_words = minor_words.lower()
    title_all = title.title()
    sentence_list = title_all.split()
    i = 1
    while i < len(sentence_list):
        if sentence_list[i].lower() in minor_words.split():
            sentence_list[i] = sentence_list[i].lower()
        i += 1
    return ' '.join(sentence_list)


print(title_case('First a of in', 'an often into'))
