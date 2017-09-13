def print_lol(thelist):
    for x in thelist:
        if isinstance(x, list):
            print_lol(x)
        else:
            print(x)
