def your_order_please(text):
    if text == '':
        return ''
    working_list = text.split()
    print(working_list)
    result = []
    for i in range(1, len(working_list) + 1):
        for j in working_list:
            if str(i) in j:
                result.append(j)
    return ' '.join(result)


print(your_order_please("4of Fo1r pe6ople g3ood th5e the2"))