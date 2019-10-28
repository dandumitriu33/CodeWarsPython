def product_fibonacci(prod):
    n = 100
    start = [0, 1]
    for i in range(1, n):
        g = start[i] + start[i-1]
        start.append(g)
    result = []
    for j in range(1, len(start) - 1):
        # print(start[j] * start[j+1])
        if start[j] * start[j+1] == prod:
            result = [start[j], start[j+1], True]
            return result
        elif start[j] * start[j+1] > prod:
            result = [start[j], start[j+1], False]
            return result


print(product_fibonacci(1234556775895))
