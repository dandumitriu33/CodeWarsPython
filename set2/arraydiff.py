def array_diff(a, b):
    if b == []:
        return a
    else:
        a_copy = a[:]
        for i in a_copy:
            for j in b:
                if i == j:
                    try:
                        a.remove(i)
                    except ValueError:
                        continue
        return a


print(array_diff([1,2,2,2,3],[2]))