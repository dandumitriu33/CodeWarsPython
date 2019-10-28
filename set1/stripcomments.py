def solution(string, markers):
    split_string = string.split('\n')
    final_list = []
    print(split_string)
    for word in split_string:
        new_word = ''
        for char in word:
            if char not in markers:
                new_word = new_word + char
            else:
                break
        final_list.append(new_word.strip())
    result = '\n'.join(final_list)
    return result 


print(solution("a #b\nc\nd $e f g", ["#", "$"]))
