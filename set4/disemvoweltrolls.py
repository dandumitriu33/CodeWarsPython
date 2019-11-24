def disemvowel(string):
    vowels = 'aeiou'
    for i in string:
        if i.lower() in vowels:
            string = string.replace(i, '')
    return string


print(disemvowel("This website is for losers LOL!"))
