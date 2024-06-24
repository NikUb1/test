def count_food(days):
    sm = 0
    for x in days:
        sm += daily_food[x - 1]
    return sm
