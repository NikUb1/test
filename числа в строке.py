def from_string_to_list(string, container):
    container.extend(list(map(int, string.split())))
