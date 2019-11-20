def highest_scoring(sentence):
    sentence_list = sentence.lower().split()

    def score(word):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        scored_alphabet = list(enumerate(alphabet, start=1))
        total = 0
        for i in word:
            for j in scored_alphabet:
                if j[1] == i:
                    total += j[0]
        return total

    highscore = score(sentence_list[0])
    highscore_word = sentence_list[0]
    for i in sentence_list:
        if score(i) > highscore:
            highscore = score(i)
            highscore_word = i
    return highscore_word


print(highest_scoring('what time are we climbing up the volcano'))
