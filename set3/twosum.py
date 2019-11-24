def two_sum(numbers, target):
    for i in numbers:
        for j in range(numbers.index(i) + 1, len(numbers)):
            if i + numbers[j] == target:
                return (numbers.index(i), j)


print(two_sum([2, 2, 3], 4))
