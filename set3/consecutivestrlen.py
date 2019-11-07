def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    max_len = 0
    result_list = []
    for i in range(n-(k-1)):
        temp_max = 0
        temp_result_list = []
        for j in range(k):
            temp_max += len(strarr[i+j])
            temp_result_list.append(strarr[i+j])
        if temp_max > max_len:
            max_len = temp_max
            result_list = temp_result_list[:]
        i += 1
    return ''.join(result_list)


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
