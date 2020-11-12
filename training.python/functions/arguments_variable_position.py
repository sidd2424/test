def foo10(*args):
    print(args)
    if (args):
        minimum_value = args[0]
        for value in args:
            if (value < minimum_value):
                minimum_value = value
        print(minimum_value)


data_set = (6, 7, 3, 5, 1)
foo10(*data_set)
