def parts_sums(ls):
    result = []
    temp_sum = sum(ls)
    for i in range(len(ls)):
        result.append(temp_sum)
        temp_sum -= ls[i]
    return result + [0]


print(parts_sums([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]))
