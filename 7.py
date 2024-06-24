def generate_park(n, m, k, p):
    # Создаем пустой парк
    park = [['.' for _ in range(m)] for _ in range(n)]

    # Функция для размещения деревьев в квадратах k x k
    def fill_square(x, y):
        trees = 0
        for i in range(x, x + k):
            for j in range(y, y + k):
                if trees < p:
                    park[i][j] = '#'
                    trees += 1
                else:
                    break

    # Размещение деревьев по всему парку
    for i in range(0, n, k):
        for j in range(0, m, k):
            fill_square(i, j)

    # Преобразуем парк в строки
    result = ["".join(row) for row in park]
    return result


# Входные данные
n, m, k, p = map(int, input().strip().split())

# Генерация парка
park = generate_park(n, m, k, p)

# Вывод результата
for row in park:
    print(row)
