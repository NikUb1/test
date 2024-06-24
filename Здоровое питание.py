def diet(racion):
    global food
    racion = racion.split(', ')
    zapr = set()
    for x in food:
        for y in x:
            zapr.add(y)
    count = 0
    for x in racion:
        if x in zapr:
            count += 1
    if count > len(racion) / 2:
        print("Не ешь столько, По!")
    else:
        print("Так держать, Воин Дракона!")

