def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    diamond_list = []
    spacing = n//2
    for i in range(1, n, 2):
        diamond_list.append(' ' * spacing + '*' * i + '\n')
        spacing -= 1
    for i in range(n, 0, -2):
        diamond_list.append(' ' * spacing + '*' * i + '\n')
        spacing += 1
    return ''.join(diamond_list)


print(diamond(3))
