def vos_pol(pol):
    t = list()
    polz = list()
    for x in range(4):
        t.append(list(pol[x * 4:(x + 1) * 4]))
    polz.append(t)
    polz.append(mirrorg(t))
    polz.append(mirrorv(t))
    polz.append(rotate(t))
    polz.append(mirrorg(mirrorv(t)))
    polz.append(mirrorg(rotate(t)))
    polz.append(mirrorv(rotate(t)))
    polz.append(mirrorg(mirrorv(rotate(t))))
    return polz


def mirrorg(pol):
    p1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(len(pol)):
        p1[x] = pol[x][::-1]
    return p1


def mirrorv(pol):
    p1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(2):
        p1[x], p1[len(pol) - 1 - x] = pol[len(pol) - 1 - x], pol[x]
    return p1


def rotate(pol):
    p1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(len(pol)):
        for y in range(len(pol[x])):
            p1[x][y] = pol[y][x]
    return p1



print(vos_pol("xxx.....x.xxx..."))