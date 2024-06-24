def print_long_words(text):
    gl = "аоэиуыеёюяaeiouy"
    m = list()
    left = 0
    for x in range(len(text)):
        if not text[x].isalpha():
            m.append(text[left:x])
            for y in range(x, len(text)):
                if text[y].isalpha():
                    left = y
                    break
    for x in m:
        k = 0
        for y in x:
            if y in gl:
                k += 1
        if k >= 4:
            print(x)

print_long_words("""whatever.wherever1solution;solut1onal""")