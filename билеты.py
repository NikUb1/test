def allocation(tup):
    ot = list()
    for x in tup:
        if places[x[0]-1][x[1]-1] == 1:
            ot.append(x)
    return ot


places = [[1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 1, 0, 0, 0]]
data = [(2, 3), (1, 4), (3, 1), (2, 3), (3, 3)]
print(allocation(data))
