def balance(left, right):
    left = left.replace('!', '2').replace('?', '3')
    right = right.replace('!', '2').replace('?', '3')
    if sum([int(i) for i in list(left)]) > sum([int(i) for i in list(right)]):
        return "Left"
    elif sum([int(i) for i in list(left)]) < sum([int(i) for i in list(right)]):
        return "Right"
    else:
        return "Balance"


print(balance('!!', '!'))
