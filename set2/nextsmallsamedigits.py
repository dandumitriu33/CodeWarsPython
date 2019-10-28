import itertools


def next_smaller(n):

    def determine_ordered_rest(n):
        n = str(n)
        work_n = list(n)
        result = []
        work_n.insert(0, 'e')
        i = 1
        while i <= len(n):
            if work_n[-i-1] == 'e':
                # result = [-1]
                i += 1
                break
            elif work_n[-i-1] == work_n[-i]:
                result.insert(0, work_n[-i])
                # print(result)
                # i += 1
            elif work_n[-i-1] > work_n[-i]:
                # result.insert(0, work_n[-i])
                if result != []:
                    result.pop(0)
                print('pre pop', result)
                return result
                break
                # result.insert(0, work_n[-i])
                # temp = work_n[-i-1]
                # work_n[-i-1] = work_n[-i]
                # work_n[-i] = temp
                # result = work_n
                # print(result)
                # i += 1
            elif work_n[-i-1] < work_n[-i]:
                result.insert(0, work_n[-i])
                
                # print(result)
                # i += 1
            i += 1
        # result = result.pop(0)
        # print('pre pop', result)
        
        return result

    def determine_operational_chunk(n):
        n = list(str(n))
        r = len(final)
        print(r)
        if r == 0:
            prefix = n[:-7]
            operation = n[-7:]
        else:
            prefix = n[:-7-r]
            operation = n[-7-r:-(r-1)]
        # 7 is the max length of permutations string
        # so that it doesn't time out
        return operation, prefix

    def smaller_than(piece):
        permutations = list(itertools.permutations(piece))
        # print(permutations)
        x = set(permutations)
        permutations = list(x)
        permutations.sort()
        # print(permutations)
        permutations.insert(0, 'e')
        g = permutations.index(tuple(piece))
        if permutations == []:
            return -1
        elif permutations[g-1] == 'e':
            return -1
        elif permutations[g-1] == '0':
            return -1
        elif int(''.join(permutations[g-1])) < 0:
            return -1
        else:
            return int(''.join(permutations[g-1]))


    if len(str(n)) < 7:
        key_piece = smaller_than(str(n))
        final = ''
    else:
        final = determine_ordered_rest(str(n))
        print(final)
    batch = determine_operational_chunk(n)
    operation = batch[0]
    prefix = batch[1]
    print(operation)
    key_piece = smaller_than(operation)
    print(key_piece)
    if key_piece == -1:
        return -1
    else:
        return int(''.join(prefix) + str(key_piece) + ''.join(final))


print(next_smaller(-100))





























# import itertools


# def next_smaller(n):

#     def short_run(n):
#         n = str(n)
#         permutations = list(itertools.permutations(n))
#         # print(permutations)
#         x = set(permutations)
#         permutations = list(x)
#         permutations.sort()
#         print(permutations)
#         permutations.insert(0, 'e')
#         g = permutations.index(tuple(n))
#         if permutations == []:
#             return -1
#         elif permutations[g-1] == 'e':
#             return -1
#         else:
#             return int(''.join(permutations[g-1]))



#     def quick_run(n):
#         n = str(n)
#         original_n = list(n)
#         working_n = list(n)
#         i = 1
#         while i <= len(n):
#             if working_n[-1] < working_n[-i]:
#                 working_n.insert(-i, working_n[-1])
#                 working_n.pop()
#                 i += 1
#                 # print(working_n)
#                 if working_n < original_n:
#                     return int(''.join(working_n))
#             else:
#                 i += 1
#                 continue
#         return 0

#     def mega_long(n):
#         n = str(n)
#         original_n = list(n)
#         working_n = list(n)
#         x = 1
#         while x < len(n):
#             working_n = list(n)
#             temp = working_n[-x]
#             working_n[-x] = working_n[-x-1]
#             working_n[-x-1] = temp
#             if working_n >= original_n:
#                 x += 1
#                 continue
#             elif working_n[0] == '0':
#                 x += 1
#                 continue
#             elif working_n == original_n:
#                 x += 1
#                 continue
#             elif working_n < original_n:
#                 return int(''.join(working_n))
#             x += 1
#         return -1

#     if len(str(n)) > 5:

#         k = mega_long(n)
#     else:
#         k = short_run(n)

#     print(k)
#     return k
    

# print(next_smaller(1234567908))





# works with most, can be done simpler
# import itertools


# def next_bigger(n):
#     n = str(n)
#     if len(n) >= 7:
#         break_point = len(n) - len(n)//3
#         if break_point > 7:
#             break_point = 7
#         a = n[:-break_point]
#         b = n[-break_point:]
#     else:
#         a = ''
#         b = n
#     # print(a + b)
#     permutations = list(itertools.permutations(b))
#     # print(permutations)
#     x = set(permutations)
#     permutations = list(x)
#     permutations.sort()
#     permutations.insert(0, (0, 0))
#     print(permutations)
#     g = permutations.index(tuple(b))
#     print(g)
#     result = list(permutations[g-1])
#     print(result)
#     if permutations == []:
#         return -1
#     elif result[0] == '0':
#         return -1
#     elif result[0] == 'e':
#         return -1
#     else:
#         return int(a + ''.join(permutations[g-1]))


# print(next_bigger(1027))



# working but too long for huge numbers

# import itertools


# def next_bigger(n):
#     n = str(n)
#     permutations = list(itertools.permutations(n))
#     g = permutations.index(tuple(n))
#     permutations.append('-1')
#     if permutations == []:
#         return -1
#     elif permutations[g] == permutations[g+1]:
#         g += 1
#         return int(''.join(permutations[g+1]))
#     else:
#         return int(''.join(permutations[g+1]))







    # print(permutations)
    # valid_list = []
    # for i in permutations:
    #     valid_number = ''.join(i)
    #     if int(valid_number) > int(n):
    #         return int(valid_number)
    # return -1
    #         valid_list.append(int(valid_number))
    # print(valid_list)
    # valid_list.sort()
    # print(valid_list)
    # if valid_list == []:
    #     return -1
    # else:
    #     return valid_list[0]

