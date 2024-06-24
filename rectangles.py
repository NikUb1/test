for _ in range(int(input())):
    n = int(input())
    j = sorted(list(map(int, input().split())))
    d = -1
    left = 0
    for r in range(3, len(j)):
        if r - left < 3:
            continue
        if j[left] == j[left + 1] and j[r] == j[r - 1]:
            tmp = ((((2 * (j[r] + j[left])) ** 2) / (j[r] * j[left])), f"{j[r]} {j[r]} {j[left]} {j[left]}")
            if d == -1:
                d = tmp
            if d > tmp:
                d = tmp
            left += 2
        if j[left] != j[left + 1]:
            while j[left] != j[left + 1] or left < r - 3:
                left += 1
        if j[r] != j[r - 1]:
            continue
    print(d[1])
