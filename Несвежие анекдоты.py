h = list()


def print_only_new(message):
    if message not in h:
        h.append(message)
        print(message)
