def swap(first, second):
    tmp = first.copy()
    first.clear()
    first.extend(second)
    second.clear()
    second.extend(tmp)
