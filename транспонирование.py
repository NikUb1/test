def transpose(matrix):
    m = matrix.copy()
    matrix.clear()
    for x in range(len(m[0])):
        tmp = list()
        for y in range(len(m)):
            tmp.append(m[y][x])
        matrix.append(tmp)
