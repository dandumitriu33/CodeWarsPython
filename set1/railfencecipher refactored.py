from random import randrange


def encode_rail_fence_cipher(string, n):
    rail = []   # generating rails
    rails = []
    i = 0
    while i < n:
        rail = []
        for j in string:
            rail.append(randrange(10))
        i += 1
        rails.append(rail)
    direction = True    # placing message on rails
    position = 0
    rail = 0
    while position < len(string):
        if direction is True:
            rails[rail][position] = string[position]
            rail += 1
            position += 1
            if rail == n-1:
                direction = False
        elif direction is False:
            rails[rail][position] = string[position]
            rail -= 1
            position += 1
            if rail == 0:
                direction = True
    i = 0   # begin encription, read rail by rail
    j = 0
    k = 0
    bingobongo = []
    encrypted_string = []
    v = 0
    for q in range(1, 300, 2):
        if v < n-1:
            bingobongo.append(q)
            v += 1
        else:
            break
    bingobongo.sort()
    bingobongo.reverse()   # from big to small
    bingo = 0
    bongo = 0
    while i < n:
        j = i
        j_counter = True
        while j < len(rails[i]) and k < len(string):
            if i == 0:
                bingo = bingobongo[0] + 1
                encrypted_string.append(rails[i][j])
                j += bingo
                k += 1
            elif i > 0 and i < (n-1):
                bingo = bingobongo[i] + 1
                bongo = bingobongo[-i] + 1
                encrypted_string.append(rails[i][j])
                if j_counter is True:
                    j += bingo
                    j_counter = False
                elif j_counter is False:
                    j += bongo
                    j_counter = True
                k += 1
            elif i == n-1:
                bingo = bingobongo[0] + 1
                encrypted_string.append(rails[i][j])
                j += bingo
                k += 1
        i += 1
    result = ''.join(encrypted_string)
    return result


# print(encode_rail_fence_cipher("Hello, World!", 4))


def decode_rail_fence_cipher(string, n):
    rail = []   # generate rails
    rails = []
    i = 0
    while i < n:
        rail = []
        for j in string:
            rail.append(randrange(10))
        i += 1
        rails.append(rail)
    i = 0   # placing encoded message on rails
    j = 0
    k = 0
    bingobongo = []
    v = 0
    for q in range(1, 300, 2):
        if v < n-1:
            bingobongo.append(q)
            v += 1
        else:
            break
    bingobongo.sort()
    bingobongo.reverse()   # from big to small
    bingo = 0
    bongo = 0
    while i < n:
        j = i
        j_counter = True
        while j < len(rails[i]) and k < len(string):
            if i == 0:
                bingo = bingobongo[0] + 1
                rails[i][j] = string[k]
                j += bingo
                k += 1
            elif i > 0 and i < (n-1):
                bingo = bingobongo[i] + 1
                bongo = bingobongo[-i] + 1
                rails[i][j] = string[k]
                if j_counter is True:
                    j += bingo
                    j_counter = False
                elif j_counter is False:
                    j += bongo
                    j_counter = True
                k += 1
            elif i == n-1:
                bingo = bingobongo[0] + 1
                rails[i][j] = string[k]
                j += bingo
                k += 1
        i += 1
    direction = True    # directional decoding, rail hop
    position = 0
    rail = 0
    result = ''
    while position < len(string):
        if rail == 0:
            direction = True
        elif rail == n-1:
            direction = False
        if direction is True:
            letter = str(rails[rail][position])
            result = result + letter
            rail += 1
        elif direction is False:
            letter = str(rails[rail][position])
            result = result + letter
            rail -= 1
        position += 1
    return result


# print(decode_rail_fence_cipher("H !e,Wdloollr", 4))
