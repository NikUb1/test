def vos_pol(pol):
    t = list()
    polz = list()
    for x in range(4):
        t.append(list(pol[x * 4:(x + 1) * 4]))
    polz.append(t)
    d = dict()
    d[0] = mirrorg
    d[1] = mirrorv
    d[2] = rotate
    for x in range(1, 8):
        m = ("00" + str(bin(x))[2:])[-3:]  # двоичные числа меньше 8 дадут все возможные комбинации из 3 эл-тов ровно 7
        p = t.copy()
        for y in range(3):
            if m[y] == "1":
                p = d[y](p)
        polz.append(p)
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
    p1 = list()
    for x in range(len(pol)):
        strok = list()
        for y in range(len(pol[x])):
            strok.append(pol[y][x])
        p1.append(strok)
    return p1


t = vos_pol("""xxx.....x.xxx...""")
for x in range(8):
    for y in range(4):
        print(''.join(t[x][y]))
    print()
