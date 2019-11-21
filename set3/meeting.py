def meeting(s):
    list_of_names = s.split(';')
    separated_list = []
    last_name_first = []
    for i in list_of_names:
        separated_list.append(tuple(i.upper().split(':')))
    for i in separated_list:
        last_name_first.append(('(' + i[1] + ', ' + i[0] + ')'))
    last_name_first.sort()
    return ''.join(last_name_first)


print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
