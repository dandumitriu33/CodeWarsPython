def string_mix(s1, s2):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'x', 'y', 'w', 'z']
    final_list = []
    for i in alphabet:
        compare_one = s1.count(i)
        compare_two = s2.count(i)
        if compare_one <= 1 and compare_two <= 1:
            continue
        elif compare_one == compare_two:
            final_list.append(f'=:{i*compare_one}')
        elif compare_one > compare_two:
            final_list.append(f'1:{i*compare_one}')
        elif compare_one < compare_two:
            final_list.append(f'2:{i*compare_two}')
        else:
            continue
    final_list.sort()

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if len(arr[j]) < len(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    result = bubble_sort(final_list)
    result = '/'.join(final_list)
    return result


print(string_mix("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"))
