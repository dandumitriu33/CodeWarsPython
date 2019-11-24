def highest_rank(arr):
    high_rank = arr[0]
    for i in arr:
        if arr.count(i) > arr.count(high_rank):
            high_rank = i
        elif arr.count(i) == arr.count(high_rank):
            if i > high_rank:
                high_rank = i
    return high_rank


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
