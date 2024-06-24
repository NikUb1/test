spis = dict()


def get_transactions(t):
    if t != "print_it":
        pst = t.split("-")[1]
        trans = pst.split(":")[0]
        sm = int(pst.split(":")[1])
        if trans not in spis:
            spis[trans] = [sm, 1]
        else:
            spis[trans][0] += sm
            spis[trans][1] += 1
    else:
        for x in spis:
            print(f"{spis[x][1]} {x} {spis[x][0]}")
