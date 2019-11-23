def score_throws(radiuses):
    if radiuses == []:
        return 0
    points = 0
    bonus_100 = True
    for i in radiuses:
        if i > 10:
            bonus_100 = False
        elif 5 <= i <= 10:
            points += 5
            bonus_100 = False
        elif i < 5:
            points += 10
    if bonus_100:
        points += 100
    return points


print(score_throws([1, 5, 11]))
