def iq_test(text):
    working_list = text.split()
    evens = []
    odds = []
    for i in working_list:
        if int(i) % 2 == 0:
            evens.append(i)
        elif int(i) % 2 != 0:
            odds.append(i)
    if len(evens) == 1:
        result = working_list.index(evens[0])
        return result + 1
    elif len(odds) == 1:
        result = working_list.index(odds[0])
        return result + 1


print(iq_test("2 4 7 8 10"))
