def find_short(s):
    s_list = s.split()
    length = len(s_list[0])
    for i in s_list:
        if len(i) < length:
            length = len(i)
    return length


print(find_short("bitcoin take over the world maybe who knows perhaps"))


def find_shorter(string):
    return min(map(len, string.split()))


print(find_short("bitcoin take over the world maybe who knows perhaps"))
