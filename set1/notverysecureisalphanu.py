def alphanumeric(password):
    if password.isalnum() is True:
        return True
    else:
        return False


print(alphanumeric('PassW0rd'))
