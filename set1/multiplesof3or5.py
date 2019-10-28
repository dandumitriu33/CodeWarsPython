def solution(number):
    multiples = set()
    div_sum = 0
    i = 1
    while i < number:
        if i % 3 == 0 or i % 5 == 0:
            multiples.add(i)
        i += 1
    div_sum = sum(multiples)
    return div_sum


print(solution(10))
