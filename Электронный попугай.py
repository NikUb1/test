phrases = list()


def parrot(phrase):
    if phrase not in phrases:
        phrases.append(phrase)
    else:
        print(phrase)
