MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
              '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
              '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.',
              '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
              '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
              '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
              '.--.-.': '@', '...---...': 'SOS'}


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    readable_word = []
    readable_sentence = []
    list_of_words = morse_code.split('   ')
    for word in list_of_words:
        list_of_letters = word.split()
        print(list_of_letters)
        for letter in list_of_letters:
            readable_word.append(MORSE_CODE[str(letter)])
        if readable_word != []:
            readable_sentence.append(''.join(readable_word))
        readable_word = []    
        # readable_sentence.append(readable_word)
    human_readable_sentence = ' '.join(readable_sentence)

    return human_readable_sentence            # morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')


print(decodeMorse('   .   .'))










#     i = 0
#    morse_letter = ''
#    while i < len(morse_code):
#        for character in morse_code:
#            if character != ' ':
#                morse_letter.strip()
#                morse_letter = morse_letter + character
#            elif character == ' ' and morse_letter[-1] != ' ':
#                print(MORSE_CODE[str(morse_letter)])
#                morse_code.replace(morse_letter, MORSE_CODE[str(morse_letter)])
#                morse_letter = character
#            elif character == ' ' and len(morse_letter) == 1 and morse_letter == ' ':
#                morse_letter = morse_letter + character
#            elif character == ' ' and len(morse_letter) == 2 and morse_letter == '  ':
#                morse_code.replace(morse_letter, ' ')
#                morse_letter = ''
#            else:
#                continue
#        i += 1