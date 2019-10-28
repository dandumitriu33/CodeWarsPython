def tribonacci(signature, n):
    if n == 0:
        return []
    g = 0
    for i in range(2, n):
        g = signature[i] + signature[i-1] + signature[i-2]
        signature.append(g)
    return signature[:n]


print(tribonacci([1, 1, 0], 8))
    