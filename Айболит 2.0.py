ok = dict()


def hello(name):
    global query
    for x in range(len(query)):
        if None == query[x]:
            print(f"Здравствуйте, {name}! Подойдите к окошку номер {x + 1}")
            query[x] = 1
            ok[name] = x
            break
    else:
        print(f"Простите, {name}, дождитесь своей очереди")


def search_card(name):
    if name in base:
        print(f"Ваша карта с номером {base.index(name) + 1} найдена")
    else:
        print("Ваша карта не найдена")
        query[ok[name]] = None


base = ["Иван", "Юлия Иванкова"]
query = [None, None, None]
hello("Иван")
search_card("Иван")
hello("Юлия Иванова")
search_card("Юлия Иванова")
