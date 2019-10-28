def duplicate_count(text):
    # Your code goes here
    i = 0
    duplicates = []
    checked_letters = []
    while i < len(text):
        if text[i].lower() in checked_letters:
            i += 1
            continue
        else:
            checked_letters.append(text[i].lower())
            rest_of_text = text[i+1:]
            for letter in rest_of_text:
                g = text[i]
                if g.lower() == letter.lower():
                    duplicates.append(text[i])
                    break
                else:
                    checked_letters.append(g)
                    continue
        i += 1
    number_of_duplicates = len(duplicates)
    return number_of_duplicates


print(duplicate_count('indivisibility11Ss'))
