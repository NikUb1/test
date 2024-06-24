def make_shades(alley, k):
    if k < 0:
        return make_shades(alley[::-1], abs(k))[::-1]
    b = [False] * len(alley)
    for x in range(len(alley)):
        if alley[x] != 0:
            if alley[x] * k + x > len(alley) - 1:
                alley[x] = len(alley) - 1 - x
            b[x:x + (alley[x] * k) + 1] = [True] * (alley[x] * k + 1)
    return b[:len(alley)]


def calculate_sunny_length(shades):
    return shades.count(False)


def main():
    k = int(input())
    alley = list(map(int, input().split()))
    if calculate_sunny_length(make_shades(alley, k)) < 10:
        print("Тени достаточно")
    else:
        print("Обгорел")
