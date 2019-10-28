def namelist(arr):
    mega_list = str(arr)
    step1 = mega_list.replace("{'name': '", '')
    step2 = step1.replace("'}", ' ')
    step3 = step2.replace("[", '')
    step4 = step3.replace("]", '')
    step5 = step4.replace(' ', '')
    farr = step5.split(",")
    # print(farr)
    last_list = []
    if len(farr) == 0:
        return ''
    elif len(farr) == 1:
        return farr[0]
    elif len(farr) == 2:
        return f'{farr[0]}, {farr[1]}'
    else:
        for i in range(0, len(farr) - 1):
            tempy = farr[i]
            last_list.append(tempy)
        temp = ', '.join(last_list)
        result = temp + ' & ' + farr[-1]
        return result


print(namelist([ {'name': 'Bart'}, {'name': 'Bart'}, {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))