def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)
    return arr
