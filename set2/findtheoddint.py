def find_the_odd(numbers):
    for i in numbers:
        x = numbers.count(i)
        if x % 2 != 0:
            return i


print(find_the_odd([3, 3, 5, 4, 5, 4, 6, 4, 6]))