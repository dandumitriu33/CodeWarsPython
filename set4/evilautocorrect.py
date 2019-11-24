import re


def autocorrect(inputs):
    inputs = re.sub('\su\s', ' your sister ', inputs)
    inputs = re.sub('^u\s', 'your sister ', inputs)
    inputs = re.sub('\su$', ' your sister', inputs)
    inputs = re.sub('^u$', 'your sister', inputs)    
    inputs = re.sub('\syou\s', ' your sister ', inputs)
    inputs = re.sub('^you\s', 'your sister ', inputs)
    inputs = re.sub('\syou$', ' your sister', inputs)
    inputs = re.sub('^you$', 'your sister', inputs)
    inputs = re.sub('^You\s', 'your sister ', inputs)
    inputs = re.sub('\syou!', ' your sister!', inputs)
    inputs = re.sub('^Yo[u]{2,}', 'your sister', inputs)
    inputs = re.sub('yo[u]{2,}', 'your sister', inputs)
    return inputs
    return inputs


# print(autocorrect('u'))
# print(autocorrect('ipsum u lorem'))
# print(autocorrect('you'))
# print(autocorrect('Youuuuuu'))
# print(autocorrect('youtube'))
# print(autocorrect('I miss you!'))
# print(autocorrect('the bayou with'))
# print(autocorrect('You should'))

print(autocorrect('U'))
