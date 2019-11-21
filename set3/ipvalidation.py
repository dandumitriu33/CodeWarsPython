def is_valid_IP(strng):
    if strng == '':
        return False
    for char in strng:
        if char != '.' and char.isdigit() is False:
            return False
    ip_list = strng.split('.')
    if len(ip_list) != 4:
        return False
    for i in ip_list:
        if len(i) > len(str(int(i))):
            return False
        if int(i) not in range(0, 256):
            return False
    return True


print(is_valid_IP('aaa'))
